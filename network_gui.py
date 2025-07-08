import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import os

# Streamlit setup
st.set_page_config(page_title="Cyber-Range Visualizer", layout="wide")
st.title("🕷️ Cyber-Range Network Visualization")

# Create a PyVis network (undirected edges)
net = Network(height="750px", width="100%", directed=False)
net.barnes_hut()

# Node info with IP addresses
nodes = {
    "attacker": {"ip": "172.30.0.10", "color": "#e53935", "shape": "diamond"},
    "router": {"ip": "172.30.0.1 / 172.31.0.1", "color": "#ffb300", "shape": "star"},
    "firewall": {"ip": "172.31.0.2 / 172.32.0.1", "color": "#6d4c41", "shape": "hexagon"},
    "victim": {"ip": "172.32.0.10", "color": "#000000", "shape": "box"},
    "victim1": {"ip": "172.32.0.11", "color": "#000000", "shape": "box"},
    "victim2": {"ip": "172.32.0.12", "color": "#000000", "shape": "box"},
}

# Add nodes with label and tooltip showing IP
for name, props in nodes.items():
    net.add_node(
        name,
        label=f"{name.upper()}\n{props['ip']}",
        title=f"{name.upper()} - {props['ip']}",
        shape=props["shape"],
        color=props["color"],
        font={"size": 20, "bold": True, "color": "#333"}
    )

# Define undirected edges
edges = [
    ("attacker", "router"),
    ("router", "firewall"),
    ("firewall", "victim"),
    ("firewall", "victim1"),
    ("firewall", "victim2"),
]

for src, dst in edges:
    net.add_edge(src, dst)

# Save HTML to temp file
with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
    tmp_path = tmp_file.name
    net.write_html(tmp_path, notebook=False)

# Embed into Streamlit
with open(tmp_path, "r", encoding="utf-8") as f:
    html = f.read()
    components.html(html, height=750, scrolling=True)

# Cleanup temp file
os.unlink(tmp_path)