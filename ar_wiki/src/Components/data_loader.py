import json
from ar_wiki.src.config import PROJECT_ROOT

def load_data():
    file_name = PROJECT_ROOT / "data" / "units.json"
    with open(file_name, 'r') as file:
        data = json.load(file)
        return data