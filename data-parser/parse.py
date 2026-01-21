import json
import os

FOLDERS_TO_PROCESS = {
    "Items": "items.json",
    "Units": "units.json",
    "Map": "maps.json"
}

START_MARKER = '[=['
END_MARKER = ']=]'

def extract_json_from_lua(file_path):
    """Extracts the JSON string inside the Roblox [=[ ]=] markers."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if START_MARKER in content and END_MARKER in content:
                raw_json = content.split(START_MARKER)[1].split(END_MARKER)[0]
                return json.loads(raw_json)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    return None

def process_category(folder_name, output_filename):
    """Scans a folder for .lua files and merges them into one JSON file."""
    if not os.path.exists(folder_name):
        print(f"Skipping {folder_name}: Folder not found.")
        return

    category_data = {}
    print(f"Processing {folder_name}...")
    files = sorted([f for f in os.listdir(folder_name) if f.endswith(".lua")])

    for file in files:
        file_path = os.path.join(folder_name, file)
        data = extract_json_from_lua(file_path)
        
        if data:
            category_data.update(data)
            print(f"  + Successfully parsed {file}")

    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(category_data, f, indent=4, ensure_ascii=False)
    
    print(f"--- Saved {len(category_data)} entries to {output_filename} ---\n")

if __name__ == "__main__":
    for folder, output in FOLDERS_TO_PROCESS.items():
        process_category(folder, output)
    
    print("All tasks complete.")