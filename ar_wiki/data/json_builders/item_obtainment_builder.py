import json
import re
from collections import defaultdict
from ar_wiki.src.config import PROJECT_ROOT

item_file = PROJECT_ROOT / "data" / "cleaned_data" / "items.json"
drop_file = PROJECT_ROOT / "data" / "cleaned_data" / "dropdata.json"

with open(item_file, 'r') as f:
    item_json = json.load(f)

with open(drop_file, 'r') as f:
    drop_json = json.load(f)

item_locations = defaultdict(set)

for stage_name, data in drop_json.items():
    stage_type = data.get("Type")

    items_found = set()
    if stage_type == "Static":
        items_found.update(data.get("Items", {}).keys())
    elif stage_type == "DifficultyBased":
        for diff_data in data.get("Difficulties", {}).values():
            items_found.update(diff_data.get("Items", {}).keys())

    for item in items_found:
        item_locations[item].add(stage_name)

def condense_obtainment(stages):
    grouped = defaultdict(list)
    others = []

    for s in stages:
        match = re.match(r"(.+)_(\d+)$", s)
        if match:
            base, num = match.groups()
            grouped[base].append(int(num))
        else:
            others.append(s)

    result = []
    for base, nums in grouped.items():
        nums.sort()
        if len(nums) > 1:
            result.append(f"{base} Act {nums[0]}-{nums[-1]}")
        else:
            result.append(f"{base} Act {nums[0]}")
    
    return sorted(result + others)

for item_name, item_info in item_json.items():
    if item_name in item_locations:
        item_info["Obtainment"] = condense_obtainment(item_locations[item_name])
    else:
        item_info["Obtainment"] = ["Not currently dropped"]

with open(item_file, 'w') as f:
    json.dump(item_json, f, indent=4)

print("items.json has been updated")