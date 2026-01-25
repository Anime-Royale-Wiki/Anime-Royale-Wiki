import json
import os

FOLDERS_TO_PROCESS = {
    "Units": "units.json",
    "Items": "items.json",
    "Map": "maps.json",
    "EvoData": "evodata.json",
    "DropData": "dropdata.json"
}

START_MARKER = '[=['
END_MARKER = ']=]'

def extract_json_from_lua(file_path):
    """Extracts and parses the JSON string inside Roblox [=[ ]=] markers."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if START_MARKER in content and END_MARKER in content:
                raw_json = content.split(START_MARKER)[1].split(END_MARKER)[0]
                return json.loads(raw_json)
    except json.JSONDecodeError as e:
        print(f"  ! JSON Error in {file_path}: {e}")
    except Exception as e:
        print(f"  ! General Error in {file_path}: {e}")
    return None

def process_category(root_folder, output_filename):
    """Walks through the folder and subfolders to merge all data."""
    if not os.path.exists(root_folder):
        print(f"Skipping {root_folder}: Folder not found.")
        return

    category_data = {}
    print(f"Processing folder: {root_folder}...")

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".lua"):
                file_path = os.path.join(root, file)
                data = extract_json_from_lua(file_path)
                
                if data:
                    relative_path = os.path.relpath(root, root_folder)
                    
                    if relative_path == ".":
                        category_data.update(data)
                    else:
                        current_dict = category_data
                        path_parts = relative_path.split(os.sep)
                        
                        for part in path_parts:
                            if part not in current_dict:
                                current_dict[part] = {}
                            current_dict = current_dict[part]
                        
                        current_dict.update(data)
                    
                    print(f"  + Merged {file}")

    if category_data:
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(category_data, f, indent=4, ensure_ascii=False)
        print(f"--- Saved {output_filename} successfully ---\n")
    else:
        print(f"--- No data found in {root_folder} ---\n")

if __name__ == "__main__":
    print("--- Starting Data Merge ---\n")
    for folder, output in FOLDERS_TO_PROCESS.items():
        process_category(folder, output)
    print("All tasks complete.")