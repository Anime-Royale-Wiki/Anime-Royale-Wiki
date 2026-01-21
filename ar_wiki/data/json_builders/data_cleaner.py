import json
import re
from ar_wiki.src.config import PROJECT_ROOT

raw_unit_file = PROJECT_ROOT / "data" / "raw_data" / "raw_units.json"
raw_item_file = PROJECT_ROOT / "data" / "raw_data" / "raw_items.json"
raw_map_file = PROJECT_ROOT / "data" / "raw_data" / "raw_maps.json"
unit_descriptions_file = PROJECT_ROOT / "data" / "cleaned_data" / "unit_description.json"

clean_unit_file = PROJECT_ROOT / "data" / "cleaned_data" / "units.json"
clean_item_file = PROJECT_ROOT / "data" / "cleaned_data" / "items.json"
clean_map_file = PROJECT_ROOT / "data" / "cleaned_data" / "maps.json"

def clean_units(raw_json_path, unit_description_path, output_path):
    with open(raw_json_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    with open(unit_description_path, 'r', encoding='utf-8') as f:
        unit_description = json.load(f)

    cleaned_db = {}

    for unit_id, source in raw_data.items():
        display_name = re.search(r'DisplayName\s*=\s*"([^"]+)"', source)
        rarity = re.search(r'Rarity\s*=\s*"([^"]+)"', source)
        
        element_match = re.search(r'Type\s*=\s*TypeList\.(\w+)', source)
        element = element_match.group(1) if element_match else "None"

        unit_entry = {
            "Name": display_name.group(1) if display_name else unit_id,
            "Rarity": rarity.group(1) if rarity else "N/A",
            "Element": element,
            "Description": unit_description[unit_id]["Description"],
            "OptimalTrait": unit_description[unit_id]["OptimalTrait"],
            "Passives": [],
            "Upgrades": []
        }

        passives_section = re.search(r'PassivesData\s*=\s*\{(.*?)\n\t\},', source, re.DOTALL)
        if passives_section:
            section_content = passives_section.group(1)
            passive_blocks = re.findall(r'\[\d+\]\s*=\s*\{(.*?)\}', section_content, re.DOTALL)
            for block in passive_blocks:
                p_title = re.search(r'Title\s*=\s*"([^"]+)"', block)
                p_desc = re.search(r'Description\s*=\s*"(.*?)"', block, re.DOTALL)
                if p_title and p_desc:
                    unit_entry["Passives"].append({
                        "Title": p_title.group(1),
                        "Description": p_desc.group(1).replace('\\n', ' ').replace('<i>', '').replace('</i>', '').strip()
                    })

        anchor_match = re.search(r'PlacementLimit\s*=\s*\d+', source)
        stat_source = source[anchor_match.end():] if anchor_match else source

        parts = re.split(r'\[(\d+)\]\s*=\s*\{', stat_source)
        for i in range(1, len(parts), 2):
            level_index = int(parts[i])
            content = parts[i+1]
            stats = {"Level": level_index}
            found_any = False
            
            for s in ["Cost", "Damage", "Range", "SPA", "Healing"]:
                pattern = fr'{s}\s*=\s*([\d\.]+|math\.huge)'
                match = re.search(pattern, content)
                if match:
                    val = match.group(1)
                    stats[s] = "∞" if val == "math.huge" else (float(val) if '.' in val else int(val))
                    found_any = True

            status_match = re.search(r'StatusList\s*=\s*\{(.*?)\}', content)
            if status_match:
                raw_statuses = re.findall(r'"([^"]+)"', status_match.group(1))
                stats["Status"] = raw_statuses
            
            if found_any and any(k in stats for k in ["Cost", "Damage", "Healing"]):
                unit_entry["Upgrades"].append(stats)

        unit_entry["Upgrades"] = sorted(unit_entry["Upgrades"], key=lambda x: x['Level'])
        cleaned_db[unit_id] = unit_entry

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_db, f, indent=4)
    
    print(f"Unit Data Cleaned. Processed {len(cleaned_db)} units.")

def clean_items(raw_item_path, output_path):
    with open(raw_item_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    cleaned_items = {}

    for item_id, source in raw_data.items():
        item_class = re.search(r'Class\s*=\s*"([^"]+)"', source)
        rarity = re.search(r'Rarity\s*=\s*"([^"]+)"', source)
        description = re.search(r'Description\s*=\s*"([^"]+)"', source)
        can_trade = re.search(r'CanTrade\s*=\s*(\w+)', source)

        cleaned_items[item_id] = {
            "Name": item_id,
            "Class": item_class.group(1) if item_class else "N/A",
            "Rarity": rarity.group(1) if rarity else "Common",
            "Description": description.group(1) if description else "",
            "CanTrade": True if can_trade and can_trade.group(1) == "true" else False
        }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_items, f, indent=4)
    
    print(f"Item Clean Complete. Processed {len(cleaned_items)} items.")

def clean_maps(raw_map_path, output_path):
    with open(raw_map_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    cleaned_maps = {}

    for map_id, source in raw_data.items():
        if "LevelingCastleAutoGeneratedFloors" in source:
            continue

        description = re.search(r'Description\s*=\s*"([^"]+)"', source)
        map_req = re.search(r'MapRequired\s*=\s*"([^"]+)"', source)
        act_matches = re.findall(r'\[\d+\]\s*=\s*"([^"]+)"', source)

        cleaned_maps[map_id] = {
            "Name": map_id,
            "Type": description.group(1) if description else ("Story" if act_matches else "Special"),
            "MapRequired": map_req.group(1) if map_req else None,
            "Acts": act_matches if act_matches else []
        }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_maps, f, indent=4)
    
    print(f"Map Clean Complete. Processed {len(cleaned_maps)} maps.")

clean_units(raw_unit_file, unit_descriptions_file, clean_unit_file)
clean_items(raw_item_file, clean_item_file)
clean_maps(raw_map_file, clean_map_file)