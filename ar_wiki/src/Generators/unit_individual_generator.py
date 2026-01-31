from jinja2 import Environment, FileSystemLoader
from ar_wiki.src.Components.data_loader import load_unit_data
from ar_wiki.src.config import PROJECT_ROOT
import re

def update_unit_grid():
    unit_data = load_unit_data()
    template_dir = PROJECT_ROOT / "Templates"
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("unit_individual_template.html")

    for unit_id, unit_info in unit_data.items():
        final_output = template.render(unit=unit_info)

        clean_name = unit_info["Name"].lower().replace(" ", "-")
        clean_name = re.sub(r'[^a-z0-9%\-]', '', clean_name)
        filename = f"{clean_name}.md"

        output_path = PROJECT_ROOT / "docs" / "units" / filename

        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_output)
            
    print(f"Success: Rebuilt {len(unit_data)} unit pages")

if __name__ == "__main__":
    update_unit_grid()