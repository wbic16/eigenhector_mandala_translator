import os
import json
import re
import glob
import corpus_config

# Configuration
CORPUS_ROOT = corpus_config.get_base_dir()
REGISTRY_FILE = corpus_config.get_registry_path()

# Sensory Keywords Dictionary
SENSE_KEYWORDS = {
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

def index_mandala(user_alias, user_data):
    print(f"Indexing mandala for: {user_alias}")
    
    docs_dir = os.path.join(CORPUS_ROOT, user_alias, "docs")
    indices_dir = os.path.join(CORPUS_ROOT, user_alias, "indices")
    
    if not os.path.exists(docs_dir):
        print(f"Warning: Docs directory not found for {user_alias} at {docs_dir}")
        return

    os.makedirs(indices_dir, exist_ok=True)
    
    sense_index = {sense: [] for sense in SENSE_KEYWORDS}
    
    doc_files = glob.glob(os.path.join(docs_dir, "*.md"))
    
    for doc_path in doc_files:
        doc_filename = os.path.basename(doc_path)
        try:
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Create a map of character offset to line number
            # Line numbers are 1-indexed
            newline_offsets = [i for i, char in enumerate(content) if char == '\n']
            
            def get_line_number(char_offset):
                for i, offset in enumerate(newline_offsets):
                    if char_offset <= offset:
                        return i + 1
                return len(newline_offsets) + 1

            sentences = extract_sentences(content)
            
            # specific strategy to find offset of sentence: 
            # This is tricky because split loses offset. 
            # Alternative: iterate through matches in the full content.
            
            # Let's use a simpler approach: Process by paragraph or line, or regex finditer on full text.
            # Given the requirement for "sentences", regex finditer of words is better.
            
            lower_content = content.lower()
            
            for sense, keywords in SENSE_KEYWORDS.items():
                for keyword in keywords:
                    # Search for the keyword in the text
                    # We utilize re.finditer to get valid locations
                    pattern = r'\b' + re.escape(keyword) + r'\b'
                    for match in re.finditer(pattern, lower_content):
                        start_pos = match.start()
                        
                        # Calculate line number
                        line_num = get_line_number(start_pos)
                        
                        # Extract context (approximate sentence)
                        # Find previous sentence delimiter
                        context_start = max(0, content.rfind('.', 0, start_pos), content.rfind('?', 0, start_pos), content.rfind('!', 0, start_pos))
                        if context_start > 0:
                             context_start += 1 # Skip the delimiter
                        
                        # Find next sentence delimiter
                        context_end = min(len(content), content.find('.', start_pos), content.find('?', start_pos), content.find('!', start_pos))
                        if context_end == -1: # Not found, try end of file
                             # If find returns -1, it means not found. min will take -1 if checked against len. 
                             # We need to handle -1s.
                             delims = [pos for pos in [content.find('.', start_pos), content.find('?', start_pos), content.find('!', start_pos)] if pos != -1]
                             context_end = min(delims) if delims else len(content)

                        if context_end < context_start: # Should happen if delimiter logic is flawed or single sentence
                            context_end = len(content)
                            
                        context = content[context_start:context_end+1].strip()
                        
                        # Clean up context if it's too long (e.g. detailed list or bad formatting)
                        if len(context) > 300:
                            context = context[:300] + "..."

                        entry = {
                            "term": keyword,
                            "context": context,
                            "doc_id": doc_filename,
                            "line_number": line_num
                        }
                        
                        # Avoid exact duplicates
                        duplicate = False
                        for existing in sense_index[sense]:
                            if existing["doc_id"] == entry["doc_id"] and existing["line_number"] == entry["line_number"] and existing["term"] == entry["term"]:
                                duplicate = True
                                break
                        
                        if not duplicate:
                            sense_index[sense].append(entry)

        except Exception as e:
            print(f"Error reading {doc_path}: {e}")

    output_path = os.path.join(indices_dir, "sense_gates.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sense_index, f, indent=2)
    
    print(f"Index saved to: {output_path}")

def main():
    registry = load_registry()
    
    # Process each user in the registry
    # Also look for directories that might not be in registry but exist (e.g. test_corpus)
    # But for now, trust registry + test_corpus
    
    for user_alias, user_data in registry.items():
        index_mandala(user_alias, user_data)
        
    # Also index test_corpus if it exists
    if os.path.exists(os.path.join(CORPUS_ROOT, "test_corpus")):
         index_mandala("test_corpus", {})

if __name__ == "__main__":
    main()
