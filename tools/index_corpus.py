import os
import json
import re
import glob
import corpus_config
import nltk
from nltk.stem import PorterStemmer

# Configuration
CORPUS_ROOT = corpus_config.get_base_dir()
REGISTRY_FILE = corpus_config.get_registry_path()

# Initialize Stemmer
stemmer = PorterStemmer()

# Thematic Keywords Dictionary
THEMES = {
    "sense_gates": {
        "sight": [
            "red", "blue", "green", "yellow", "white", "black", "purple", "orange", "pink",
            "dark", "bright", "shiny", "dull", "glowing", "shimmering", "transparent", "opaque",
            "vision", "visual", "saw", "seen", "look", "light", "color", "shadow", "image",
            "gaze", "behold", "observe", "spectrum", "radiance", "brilliance", "glimmer"
        ],
        "sound": [
            "loud", "quiet", "silent", "noisy", "whisper", "scream", "shout", "bang", "crash",
            "music", "melody", "tone", "voice", "heard", "listen", "auditory", "sound", "hum",
            "ringing", "vibration", "song", "resonance", "echo", "chorus", "rhythm", "acoustic"
        ],
        "smell": [
            "fragrant", "stinky", "scent", "odor", "perfume", "aroma", "smell", "sniff", "nose",
            "pungent", "musky", "floral", "waft", "essence", "bouquet", "reek"
        ],
        "taste": [
            "sweet", "sour", "bitter", "salty", "savory", "umami", "delicious", "disgusting",
            "taste", "flavor", "mouth", "tongue", "spicy", "acrid", "tangy", "palate"
        ],
        "touch": [
            "hard", "soft", "rough", "smooth", "hot", "cold", "warm", "wet", "dry", "texture",
            "felt", "touch", "skin", "pain", "itch", "tingle", "pressure", "sharp", "blunt",
            "tactile", "caress", "friction"
        ],
        "proprioception": [
            "heavy", "light", "floating", "sinking", "spinning", "dizzy", "balance", "movement",
            "position", "falling", "rising", "weight", "gravity", "body", "posture", "coordination"
        ],
        "interoception": [
            "heartbeat", "breath", "pulse", "hunger", "thirst", "pain", "pleasure", "emotion",
            "feeling", "gut", "stomach", "chest", "throat", "internal", "visceral", "nausea"
        ]
    },
    "magitech": {
        "resonance": ["resonance", "harmonic", "synchronization", "vibration", "echo", "attunement", "frequency", "pulse"],
        "engineering": ["engineering", "magitech", "machinery", "device", "construction", "blueprint", "circuit", "conduit", "capacitor", "emitter"],
        "archetypes": ["wordcel", "shape rotator", "scientist", "engineer", "artificer", "technician", "alchemist", "scholar"],
        "aura": ["vibe aura", "presence", "emanation", "glow", "energy", "field", "radiance", "shimmer"],
        "union": ["yab-yum", "chiral", "synthesis", "union", "duality", "mirror", "symmetry", "merging", "fusion"]
    },
    "ethics": {
        "alignment": ["authoritarian", "egalitarian", "xenophobe", "xenophile", "militarist", "pacifist", "spiritualist", "materialist", "sovereignty", "autonomy"],
        "society": ["civic", "governance", "order", "structure", "tradition", "meritocracy", "hierarchy", "collective", "individualism", "justice"],
        "evolution": ["ascension", "transcendence", "evolution", "path", "final form", "great work", "utopia", "dystopia", "enlightenment"]
    },
    "heroic": {
        "attributes": ["power", "speed", "spirit", "recovery", "strength", "agility", "vitality", "stamina", "willpower", "bravery", "courage", "fortitude"],
        "roles": ["healer", "researcher", "defender", "balancer", "tank", "support", "tactician", "leader", "scout", "assassin"],
        "mechanics": ["essence", "confluence", "soul", "rank", "ability", "skill", "mana", "cooldown", "mastery", "potential", "buff", "debuff"]
    }
}

def load_registry():
    if not os.path.exists(REGISTRY_FILE):
        print(f"Error: Registry file not found at {REGISTRY_FILE}")
        return {}
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_sentences(text):
    # Simple sentence splitting
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

def mask_content(text):
    """
    Replaces URLs and boilerplate with spaces, preserving length and offsets.
    """
    masked = text
    
    # 1. Mask URLs (http/https)
    # This regex matches http:// or https:// followed by non-whitespace characters
    def replace_with_spaces(match):
        return " " * len(match.group(0))
    
    masked = re.sub(r'https?://\S+', replace_with_spaces, masked)
    
    # 2. Mask common boilerplate lines (Substack specific)
    # Matches lines starting with specific keywords, case insensitive
    boilerplate_patterns = [
        r'^Subscribe.*$',
        r'^Share.*$',
        r'^CommentsRestacks.*$',
        r'^TopLatestDiscussions.*$',
        r'^©.*$', 
        r'^.*requires JavaScript.*$'
    ]
    
    for pattern in boilerplate_patterns:
        masked = re.sub(pattern, replace_with_spaces, masked, flags=re.MULTILINE | re.IGNORECASE)

    # 3. Mask image file extensions if they appear in text that looks like a filename
    # e.g. "default-light.png" -> "                 "
    masked = re.sub(r'[\w-]+\.(png|jpg|jpeg|gif|webp)', replace_with_spaces, masked, flags=re.IGNORECASE)

    return masked

def index_mandala(user_alias, user_data):
    print(f"Indexing mandala themes for: {user_alias}")
    
    docs_dir = os.path.join(CORPUS_ROOT, user_alias, "docs")
    indices_dir = os.path.join(CORPUS_ROOT, user_alias, "indices")
    
    if not os.path.exists(docs_dir):
        print(f"Warning: Docs directory not found for {user_alias} at {docs_dir}")
        return

    os.makedirs(indices_dir, exist_ok=True)
    
    # Pre-stem themes for matching
    stemmed_vocabulary = {}
    for t_name, cats_dict in THEMES.items():
        stemmed_vocabulary[t_name] = {}
        for c_name, kws_list in cats_dict.items():
            # Map of stem -> original keyword
            stemmed_vocabulary[t_name][c_name] = {stemmer.stem(k.lower()): k for k in kws_list}

    # Initialize separate indices for each theme
    indices = {t: {c: [] for c in cats} for t, cats in THEMES.items()}
    
    doc_files = glob.glob(os.path.join(docs_dir, "*.md"))
    
    for doc_path in doc_files:
        doc_filename = os.path.basename(doc_path)
        try:
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Create a map of character offset to line number
            newline_offsets = [i for i, char in enumerate(content) if char == '\n']
            
            def get_line_number(char_off):
                for i, off in enumerate(newline_offsets):
                    if char_off <= off:
                        return i + 1
                return len(newline_offsets) + 1

            # Create masked content for searching
            masked_content = mask_content(content)
            
            # Tokenize into words with offsets and stems
            doc_words = []
            for m in re.finditer(r'\b\w+\b', masked_content):
                w_text = m.group(0)
                doc_words.append({
                    "text": w_text,
                    "stem": stemmer.stem(w_text.lower()),
                    "start": int(m.start())
                })
            
            for t_name, t_cats in stemmed_vocabulary.items():
                for c_name, stem_to_orig in t_cats.items():
                    for w_info in doc_words:
                        w_stem = w_info["stem"]
                        if w_stem in stem_to_orig:
                            s_pos = w_info["start"]
                            ln_num = get_line_number(s_pos)
                            m_term = stem_to_orig[w_stem]
                            
                            # Extract context (sentence-based)
                            # Look back for start of sentence or paragraph
                            context_markers = ['\n', '. ', '? ', '! ']
                            c_start = 0
                            for mkr in context_markers:
                                p_back = content.rfind(mkr, 0, int(s_pos))
                                if p_back != -1:
                                    c_start = max(c_start, p_back + len(mkr))
                            
                            # Look forward for end of sentence or paragraph
                            c_end = len(content)
                            for mkr in context_markers:
                                p_fwd = content.find(mkr, int(s_pos))
                                if p_fwd != -1:
                                    c_end = min(c_end, p_fwd + len(mkr))
                            
                            context_snippet = content[c_start:c_end].strip()
                            if len(context_snippet) > 400:
                                context_snippet = context_snippet[:400] + "..."
                            
                            if not context_snippet:
                                continue

                            entry = {
                                "term": m_term,
                                "matched": w_info["text"],
                                "context": context_snippet,
                                "doc_id": doc_filename,
                                "line_number": ln_num
                            }
                            
                            # Avoid duplicates on the same line for the same theme/category
                            is_dup = False
                            for existing in indices[t_name][c_name]:
                                if existing["doc_id"] == entry["doc_id"] and \
                                   existing["line_number"] == entry["line_number"] and \
                                   existing["term"] == entry["term"]:
                                    is_dup = True
                                    break
                            
                            if not is_dup:
                                indices[t_name][c_name].append(entry)

        except Exception as e:
            print(f"Error reading {doc_path}: {e}")

    # Save each theme's index to a separate file
    for theme, data in indices.items():
        output_path = os.path.join(indices_dir, f"{theme}_index.json" if theme != "sense_gates" else "sense_gates.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Theme index [{theme}] saved to: {output_path}")

def main():
    registry = load_registry()
    
    # Process each user in the registry
    for user_alias, user_data in registry.items():
        index_mandala(user_alias, user_data)
        
    # Also index test_corpus if it exists
    if os.path.exists(os.path.join(CORPUS_ROOT, "test_corpus")):
         index_mandala("test_corpus", {})

if __name__ == "__main__":
    main()
