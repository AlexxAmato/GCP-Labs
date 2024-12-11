import yaml
from jinja2 import Environment, FileSystemLoader

# Define paths
TEMPLATES_DIR = "templates"
VARS_DIR = "vars"

# Function to load the YAML file
def load_yaml(file_name):
    with open(f"{VARS_DIR}/{file_name}", 'r') as file:
        return yaml.safe_load(file)

# Main function
def render_template(template_name, vars_file):
    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    
    # Load the template
    template = env.get_template(template_name)
    
    # Load the variables
    data = load_yaml(vars_file)
    
    # Render the template
    return template.render(data)

# Example usage
if __name__ == "__main__":
    # User selects the configuration type
    template_name = "bgp.j2"  # Or dynamically assign based on input
    vars_file = "bgp_vars.yml"

    # Generate the configuration
    rendered_config = render_template(template_name, vars_file)
    
    # Print or save the rendered configuration
    print(rendered_config)

