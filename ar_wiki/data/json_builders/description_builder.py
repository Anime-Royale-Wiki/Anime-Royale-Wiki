import json
from ar_wiki.src.config import PROJECT_ROOT

unit_description = dict()

raw_unit_data = PROJECT_ROOT / "data" / "raw_data" / "raw_units.json"
unit_description_file = PROJECT_ROOT / "data" / "cleaned_data" / "unit_description.json"

with open(raw_unit_data, 'r') as f:
    raw_file = json.load(f)

for unit_id, unit in raw_file.items():
    unit_description[unit_id] = {
        "Description": "",
        "OptimalTrait": "",
        "Obtainment": ""
    }

with open(unit_description_file, 'w') as f:
    json.dump(unit_description, f, indent=4)