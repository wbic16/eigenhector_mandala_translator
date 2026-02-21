import os
import json
import re
import glob
import corpus_config

# Configuration
CORPUS_ROOT = corpus_config.get_base_dir()
REGISTRY_FILE = corpus_config.get_registry_path()

# Thematic Keywords Dictionary
THEMES = {
    "sense_gates": {
        "sight": [
            "red", "blue", "green", "yellow", "white", "black", "purple", "orange", "pink",
            "dark", "bright", "shiny", "dull", "glowing", "shimmering", "transparent", "opaque",
            "vision", "visual", "saw", "seen", "look", "light", "color", "shadow", "image"
        ],
        "sound": [
            "loud", "quiet", "silent", "noisy", "whisper", "scream", "shout", "bang", "crash",
            "music", "melody", "tone", "voice", "heard", "listen", "auditory", "sound", "hum",
            "ringing", "vibration", "song"
        ],
        "smell": [
            "fragrant", "stinky", "scent", "odor", "perfume", "aroma", "smell", "sniff", "nose",
            "pungent", "musky", "floral"
        ],
        "taste": [
            "sweet", "sour", "bitter", "salty", "savory", "umami", "delicious", "disgusting",
            "taste", "flavor", "mouth", "tongue", "spicy"
        ],
        "touch": [
            "hard", "soft", "rough", "smooth", "hot", "cold", "warm", "wet", "dry", "texture",
            "felt", "touch", "skin", "pain", "itch", "tingle", "pressure", "sharp", "blunt"
        ],
        "proprioception": [
            "heavy", "light", "floating", "sinking", "spinning", "dizzy", "balance", "movement",
            "position", "falling", "rising", "weight", "gravity", "body"
        ],
        "interoception": [
            "heartbeat", "breath", "pulse", "hunger", "thirst", "pain", "pleasure", "emotion",
            "feeling", "gut", "stomach", "chest", "throat", "internal", "visceral"
        ]
    },
    "magitech": {
        "resonance": ["resonance", "harmonic", "synchronization", "vibration", "echo"],
        "engineering": ["engineering", "magitech", "machinery", "device", "construction", "blueprint"],
        "archetypes": ["wordcel", "shape rotator", "scientist", "engineer", "artificer"],
        "aura": ["vibe aura", "presence", "emanation", "glow", "energy"],
        "union": ["yab-yum", "chiral", "synthesis", "union", "duality", "mirror"]
    },
    "ethics": {
        "alignment": ["authoritarian", "egalitarian", "xenophobe", "xenophile", "militarist", "pacifist", "spiritualist", "materialist"],
        "society": ["civic", "governance", "order", "structure", "tradition", "meritocracy"],
        "evolution": ["ascension", "transcendence", "evolution", "path", "final form", "great work"]
    },
    "heroic": {
        "attributes": ["power", "speed", "spirit", "recovery", "strength", "agility", "vitality", "stamina"],
        "roles": ["healer", "researcher", "defender", "balancer", "tank", "support", "tactician"],
        "mechanics": ["essence", "confluence", "soul", "rank", "ability", "skill", "mana"]
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
    
    # Initialize separate indices for each theme
    indices = {theme: {category: [] for category in CATEGORIES} for theme, CATEGORIES in THEMES.items()}
    
    doc_files = glob.glob(os.path.join(docs_dir, "*.md"))
    
    for doc_path in doc_files:
        doc_filename = os.path.basename(doc_path)
        try:
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Create a map of character offset to line number
            newline_offsets = [i for i, char in enumerate(content) if char == '\n']
            
            def get_line_number(char_offset):
                for i, offset in enumerate(newline_offsets):
                    if char_offset <= offset:
                        return i + 1
                return len(newline_offsets) + 1

            # Create masked content for searching
            masked_content = mask_content(content)
            lower_masked_content = masked_content.lower()
            
            for theme, categories in THEMES.items():
                for category, keywords in categories.items():
                    for keyword in keywords:
                        # Search for the keyword in the masked text
                        pattern = r'\b' + re.escape(keyword) + r'\b'
                        for match in re.finditer(pattern, lower_masked_content):
                            start_pos = match.start()
                            line_num = get_line_number(start_pos)
                            
                            # Extract context
                            context_start = max(0, content.rfind('.', 0, start_pos), content.rfind('?', 0, start_pos), content.rfind('!', 0, start_pos))
                            if context_start > 0:
                                 context_start += 1
                            
                            context_end = min(len(content), content.find('.', start_pos), content.find('?', start_pos), content.find('!', start_pos))
                            if context_end == -1: 
                                 delims = [pos for pos in [content.find('.', start_pos), content.find('?', start_pos), content.find('!', start_pos)] if pos != -1]
                                 context_end = min(delims) if delims else len(content)

                            if context_end < context_start:
                                context_end = len(content)
                                
                            context = content[context_start:context_end+1].strip()
                            if len(context) > 300:
                                context = context[:300] + "..."
                            
                            if not context:
                                continue

                            entry = {
                                "term": keyword,
                                "context": context,
                                "doc_id": doc_filename,
                                "line_number": line_num
                            }
                            
                            # Avoid duplicates
                            duplicate = False
                            for existing in indices[theme][category]:
                                if existing["doc_id"] == entry["doc_id"] and existing["line_number"] == entry["line_number"] and existing["term"] == entry["term"]:
                                    duplicate = True
                                    break
                            
                            if not duplicate:
                                indices[theme][category].append(entry)

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
