import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components
import os

# IP mapping for display
device_ips = {
    'attacker': '172.20.0.2',
    'router': '172.20.0.254',
    'firewall': '172.18.0.2',
    'victim': '172.21.0.2',
    'victim1': '172.21.0.3',
    'victim2': '172.21.0.4',
    'home_router': '172.30.100.254',
    'home_firewall': '172.30.100.253',
    'smart_tv': '172.30.100.10',
    'smart_light': '172.30.100.11',
    'laptop': '172.30.100.20',
    'splunk': '172.30.200.100'
}

# Initialize network
net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black", directed=False)

# Core infrastructure nodes
net.add_node("attacker", label=f"attacker\n{device_ips['attacker']}", color="red", shape="ellipse")
net.add_node("router", label=f"router\n{device_ips['router']}", color="gray", shape="star")
net.add_node("firewall", label=f"firewall\n{device_ips['firewall']}", color="gray", shape="box")
net.add_node("splunk", label=f"splunk\n{device_ips['splunk']}", color="orangered", shape="hexagon")

# Victim nodes (web app targets)
for victim in ["victim", "victim1", "victim2"]:
    net.add_node(victim, label=f"{victim}\n{device_ips[victim]}", color="deepskyblue", shape="ellipse")

# Home network components
net.add_node("home_router", label=f"home_router\n{device_ips['home_router']}", color="orange", shape="star")
net.add_node("home_firewall", label=f"home_firewall\n{device_ips['home_firewall']}", color="orange", shape="box")
net.add_node("smart_tv", label=f"smart_tv\n{device_ips['smart_tv']}", color="lightblue", shape="ellipse")
net.add_node("smart_light", label=f"smart_light\n{device_ips['smart_light']}", color="yellow", shape="ellipse")
net.add_node("laptop", label=f"laptop\n{device_ips['laptop']}", color="lightgreen", shape="ellipse")

# Edges
net.add_edges([
    ("attacker", "router"),
    ("router", "firewall"),
    ("firewall", "victim"),
    ("firewall", "victim1"),
    ("firewall", "victim2"),
    ("router", "splunk"),
    ("router", "home_firewall"),
    ("home_firewall", "home_router"),
    ("home_router", "smart_tv"),
    ("home_router", "smart_light"),
    ("home_router", "laptop")
])

# Render to HTML and embed in Streamlit
output_path = os.path.join(os.getcwd(), "network_gui.html")
net.save_graph(output_path)

with open(output_path, "r", encoding="utf-8") as HtmlFile:
    components.html(HtmlFile.read(), height=800, scrolling=True)