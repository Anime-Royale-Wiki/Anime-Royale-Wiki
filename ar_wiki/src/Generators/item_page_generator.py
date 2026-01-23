from jinja2 import Environment, FileSystemLoader
from ar_wiki.src.Components.data_loader import load_item_data
from ar_wiki.src.config import PROJECT_ROOT

def update_item_grid():
    item_data = load_item_data()

    template_dir = PROJECT_ROOT / "Templates"
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("item_page_template.html")
    
    final_output = template.render(items=item_data)

    output_path = PROJECT_ROOT / "docs" / "item_page.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
            
    print(f"Success: Rebuilt {output_path.name}")

if __name__ == "__main__":
    update_item_grid()