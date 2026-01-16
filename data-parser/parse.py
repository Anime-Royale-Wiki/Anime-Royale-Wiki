import json
import os

files = ['EXPORT_PART_1.lua', 'EXPORT_PART_2.lua', 'EXPORT_PART_3.lua'] 
master_data = {}

for f_name in files:
    if not os.path.exists(f_name):
        continue
        
    with open(f_name, 'r', encoding='latin-1') as f:
        content = f.read()
        
        try:
            start_marker = '[=['
            end_marker = ']=]'
            
            if start_marker in content and end_marker in content:
                raw_json = content.split(start_marker)[1].split(end_marker)[0]
                data = json.loads(raw_json)
                master_data.update(data)
                print(f"Successfully loaded {f_name}")
            else:
                print(f"Skipping {f_name}: Could not find markers.")
        except Exception as e:
            print(f"Error parsing {f_name}: {e}")

with open('full_raw_data.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, indent=4, ensure_ascii=False)

print(f"\n--- SUCCESS ---")
print(f"Merged {len(master_data)} units into full_raw_data.json!")

print(master_data['Mirajane'])