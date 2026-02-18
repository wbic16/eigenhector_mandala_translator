import argparse
import json
import logging
from pathlib import Path
import sys

# Add the project root to sys.path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def load_schema():
    """Loads the analysis JSON template as the schema."""
    schema_path = PROJECT_ROOT / "skills" / "ANALYSIS_JSON_TEMPLATE.json"
    if not schema_path.exists():
        logging.error(f"Schema file not found at {schema_path}")
        return None
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding schema: {e}")
        return None

def validate_structure(data, schema, path="root"):
    """Recursively validates data against the schema structure."""
    if isinstance(schema, dict):
        if not isinstance(data, dict):
            logging.error(f"{path}: Expected object, got {type(data).__name__}")
            return False
        
        valid = True
        for key, value in schema.items():
            if key not in data:
                logging.error(f"{path}: Missing key '{key}'")
                valid = False
            else:
                if not validate_structure(data[key], value, path=f"{path}.{key}"):
                    valid = False
        return valid
    
    elif isinstance(schema, list):
        if not isinstance(data, list):
            logging.error(f"{path}: Expected array, got {type(data).__name__}")
            return False
        
        if schema:
            # Validate each item in the data list against the first item in the schema list (template)
            template = schema[0]
            valid = True
            for i, item in enumerate(data):
                if not validate_structure(item, template, path=f"{path}[{i}]"):
                    valid = False
            return valid
        return True
    
    else:
        # Primitive types (sanity check, although flexible in JSON)
        # We can enforce type checks here if needed, but for now existence is key.
        return True

def validate_analysis(file_path):
    """Validates the analysis JSON file."""
    path = Path(file_path)
    if not path.exists():
        logging.error(f"File not found: {file_path}")
        return False

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON: {e}")
        return False

    schema = load_schema()
    if not schema:
        return False

    logging.info(f"Validating {file_path} against schema...")
    if validate_structure(data, schema):
        logging.info("Validation Successful! The file conforms to the schema.")
        return True
    else:
        logging.error("Validation Failed. See errors above.")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate analysis JSON against the schema.")
    parser.add_argument("file_path", help="Path to the analysis JSON file")
    
    args = parser.parse_args()
    
    if validate_analysis(args.file_path):
        sys.exit(0)
    else:
        sys.exit(1)
