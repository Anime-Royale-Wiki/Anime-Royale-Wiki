import json
from ar_wiki.src.config import PROJECT_ROOT

unit_data_file = PROJECT_ROOT / "data" / "cleaned_data" / "units.json"
evolution_data_file = PROJECT_ROOT / "data" / "cleaned_data" / "evodata.json"

with open(unit_data_file, 'r') as f:
    unit_file = json.load(f)

with open(evolution_data_file, 'r') as f:
    evolution_file = json.load(f)

for unit_id, unit in unit_file.items():
    if unit_id in evolution_file:
        evolves_to = unit["EvolutionRequirements"]["EvolvesTo"]
        evolution_file[unit_id]["EvolutionName"] = unit_file[evolves_to]["Name"]

for unit_id, unit in unit_file.items():
    evo_req = unit.get("EvolutionRequirements")
    if evo_req and "EvolvesTo" in evo_req:
        evolves_to = unit["EvolutionRequirements"]["EvolvesTo"]
        unit_file[evolves_to]["EvolutionRequirements"]["EvolvesFrom"] = unit['Name']
     

with open(evolution_data_file, 'w') as f:
    json.dump(evolution_file, f, indent=4)

with open(unit_data_file, 'w') as f:
    json.dump(unit_file, f, indent=4)