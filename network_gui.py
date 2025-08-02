import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components
import os

# Extended device info
devices = {
    'attacker': {
        'name': 'Attacker',
        'ip': '10.88.10.10',
        'routes': '→ Router (10.88.10.254)',
        'color': 'red',
        'shape': 'ellipse'
    },
    'router': {
        'name': 'Router',
        'ip': '10.88.10.254 / 10.88.20.254 / 10.88.40.254',
        'routes': '← Attacker, IoT | → Firewall, Splunk',
        'color': 'gray',
        'shape': 'star'
    },
    'iot': {
        'name': 'IoT 1',
        'ip': '10.88.20.10',
        'routes': '→ Router (10.88.20.254)',
        'color': 'orange',
        'shape': 'dot'
    },
    'firewall': {
        'name': 'Firewall',
        'ip': '10.88.40.10 / 10.88.30.254',
        'routes': '← Router | → Victim, Splunk',
        'color': 'gray',
        'shape': 'box'
    },
    'victim': {
        'name': 'Victim',
        'ip': '10.88.30.10',
        'routes': '→ Firewall (10.88.30.254)',
        'color': 'deepskyblue',
        'shape': 'ellipse'
    },
    'splunk': {
        'name': 'Splunk',
        'ip': '10.88.10.200 / 10.88.20.200 / 10.88.30.200',
        'routes': 'Connected to all segments',
        'color': 'orangered',
        'shape': 'hexagon'
    }
}

# Initialize the network graph
net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black", directed=False)

# Add nodes with tooltip details
for key, info in devices.items():
    title = f"{info['name']}\nIP: {info['ip']}\nRoutes: {info['routes']}"
    net.add_node(key, label=info['name'], title=title, color=info['color'], shape=info['shape'])

# Define connections
edges = [
    ("attacker", "router"),
    ("iot", "router"),
    ("router", "firewall"),
    ("firewall", "victim"),
    ("router", "splunk"),
    ("firewall", "splunk"),
    ("victim", "splunk"),
    ("iot", "splunk")
]
net.add_edges(edges)

# Render and display
output_path = os.path.join(os.getcwd(), "network_gui_interactive.html")
net.save_graph(output_path)

with open(output_path, "r", encoding="utf-8") as HtmlFile:
    components.html(HtmlFile.read(), height=800, scrolling=True)