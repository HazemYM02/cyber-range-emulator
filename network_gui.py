import streamlit as st
from pyvis.network import Network
import docker
import tempfile
import os

st.set_page_config(page_title="Cyber-Range Network", layout="wide")
st.title("📡 Cyber-Range Docker Network Visualisation")

client = docker.from_env()
graph = Network(height="800px", width="100%", directed=False)
graph.barnes_hut()

# Role-based shapes and colors
roles = {
    "attacker": {"shape": "diamond", "color": "#e53935"},
    "attacker1": {"shape": "diamond", "color": "#e53935"},
    "attacker2": {"shape": "diamond", "color": "#e53935"},
    "victim": {"shape": "box", "color": "#000000"},
    "victim1": {"shape": "box", "color": "#000000"},
    "victim2": {"shape": "box", "color": "#000000"},
    "router": {"shape": "star", "color": "#ffb300"},
    "firewall": {"shape": "hexagon", "color": "#6d4c41"},
    "webserver": {"shape": "dot", "color": "#43a047"},
    "dns": {"shape": "dot", "color": "#43a047"},
    "siem": {"shape": "triangle", "color": "#8e24aa"},
    "workstation": {"shape": "box", "color": "#00acc1"}
}

# Add Docker networks
networks = [net for net in client.networks.list() if "cyber-range-emulator" in net.name]
for net in networks:
    graph.add_node(
        net.name,
        label=net.name,
        shape="box",
        color="#03a9f4",
        size=60,
        font={"size": 22, "bold": True}
    )

# Add Docker containers
for container in client.containers.list():
    cname = container.name
    image = container.image.tags[0] if container.image.tags else "untagged"
    net_info = container.attrs["NetworkSettings"]["Networks"]
    relevant_nets = {n: d for n, d in net_info.items() if "cyber-range-emulator" in n}
    ip_list = [d.get("IPAddress", "N/A") for d in relevant_nets.values()]
    all_ips = "\\n".join(ip_list)
    label = f"{cname}\\n{all_ips}"
    tooltip = f"{image} ({', '.join(ip_list)})"
    role = roles.get(cname, {"shape": "ellipse", "color": "#90a4ae"})

    graph.add_node(
        cname,
        label=label,
        title=tooltip,
        shape=role["shape"],
        color=role["color"],
        size=65,
        font={"size": 20, "bold": True}
    )

    for net_name in relevant_nets:
        graph.add_edge(net_name, cname, width=3)

# Render and display in Streamlit
tmp_dir = tempfile.gettempdir()
html_path = os.path.join(tmp_dir, "network_gui_updated.html")
graph.write_html(html_path, notebook=False)

with open(html_path, "r") as f:
    st.components.v1.html(f.read(), height=800, scrolling=True)