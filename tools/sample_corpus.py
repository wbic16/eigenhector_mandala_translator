import os
import random

import corpus_config

corpus_root = corpus_config.get_base_dir()
exclude = ["test_corpus", "corpus_registry.json"]
# Use current directory or specific tools directory
output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus_sample_output.txt")

with open(output_file, "w", encoding="utf-8") as out:
    for item in os.listdir(corpus_root):
        if item in exclude:
            continue
        
        item_path = os.path.join(corpus_root, item)
        if os.path.isdir(item_path):
            out.write(f"\n--- Mandala: {item} ---\n")
            files = []
            for root, dirs, filenames in os.walk(item_path):
                for filename in filenames:
                    if filename.endswith(".md") or filename.endswith(".txt"):
                         files.append(os.path.join(root, filename))
            
            # Pick 5 random files
            sample = random.sample(files, min(len(files), 5))
            
            for file_path in sample:
                out.write(f"File: {file_path}\n")
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read(1000) # Read first 1000 chars
                        out.write(content)
                        out.write("\n" + "="*20 + "\n")
                except Exception as e:
                    out.write(f"Error reading file: {e}\n")
