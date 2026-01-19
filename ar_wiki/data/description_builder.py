import json

unit_description = dict()

with open('full_raw_data.json', 'r') as f:
    raw_file = json.load(f)

for unit_id, unit in raw_file.items():
    unit_description[unit_id] = {
        "Description": "",
        "OptimalTrait": "",
        "Obtainment": ""
    }

with open('unit_description.json', 'w') as f:
    json.dump(unit_description, f, indent=4)