import yaml
from jinja2 import Environment, FileSystemLoader

# Load data from the YAML file
with open('bgp_vars.yml', 'r') as file:
    data = yaml.safe_load(file)

# Set up the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'))  # The '.' points to the current directory
template = env.get_template('bgp.j2')  # Reference the Jinja2 template file

# Render the template
rendered_config = template.render(data)

# Print the rendered configuration
print(rendered_config)


