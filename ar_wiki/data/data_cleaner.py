import json
import re

def clean_and_transform(raw_json_path, output_path):
    with open(raw_json_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

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
    
    print(f"Purge complete. Cleaned {len(cleaned_db)} units into {output_path}")

clean_and_transform('full_raw_data.json', 'units.json')