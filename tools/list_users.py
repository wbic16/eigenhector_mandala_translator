import json
import os

def load_registry(storage_root=None):
    if storage_root:
        base_dir = storage_root
    else:
        # Default to reports/mystic_corpus in the project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        base_dir = os.path.join(project_root, 'reports', 'mystic_corpus')
            
    registry_path = os.path.join(base_dir, 'corpus_registry.json')
    if os.path.exists(registry_path):
        with open(registry_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def main():
    registry = load_registry()
    
    print(f"{'ALIAS':<15} {'TYPE':<15} {'DESCRIPTION'}")
    print("-" * 60)
    
    if not registry:
        print("No users found in registry.")
        return

    for alias, data in registry.items():
        type_str = data.get('type', 'unknown')
        desc = data.get('description', '')
        print(f"{alias:<15} {type_str:<15} {desc}")

if __name__ == "__main__":
    main()
