from jinja2 import Template

# Load the Jinja2 template
bgp_template = """
router bgp {{ local_as }}
  neighbor {{ neighbor_ip }} remote-as {{ neighbor_as }}
  {% if next_hop_self %}
  neighbor {{ neighbor_ip }} next-hop-self
  {% endif %}
  {% if update_source %}
  neighbor {{ neighbor_ip }} update-source {{ update_source }}
  {% endif %}
  {% for network in advertised_networks %}
  network {{ network }}
  {% endfor %}
"""

# Define the data for the template
data = {
    "local_as": 10,
    "neighbor_ip": "1.1.1.10",
    "neighbor_as": 22,
    "next_hop_self": True,
    "update_source": "Ethernet1",
    "advertised_networks": [
        "10.1.1.0/24",
        "10.1.2.0/24",
        "10.1.3.0/24",
        "10.1.4.0/24"
    ]
}

# Render the template
template = Template(bgp_template)
rendered_config = template.render(data)

print(rendered_config)

