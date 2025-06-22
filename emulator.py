import docker
import yaml

# Initialize Docker client
client = docker.from_env()

def load_topology():
    with open("topology.yaml", "r") as file:
        return yaml.safe_load(file)

def create_container(node):
    try:
        container = client.containers.run(
            image=node["image"],
            name=node["name"],
            command="sleep infinity",
            tty=True,
            detach=True,
            network="bridge"  # Replace with your network if custom
        )
        print(f"[+] Started container: {node['name']}")
        return container
    except docker.errors.APIError:
        print(f"[!] Container '{node['name']}' already running or exists.")
        return client.containers.get(node["name"])

def run_command(container, command):
    print(f"[>] {container.name}: {command}")
    output = container.exec_run(command)
    print(output.output.decode())

def cleanup(containers):
    for c in containers.values():
        c.kill()
        c.remove()
        print(f"[-] Removed {c.name}")

def main():
    topology = load_topology()
    containers = {}

    # Create containers
    for node in topology["nodes"]:
        containers[node["name"]] = create_container(node)

    # Example commands to test tool installations
    run_command(containers["attacker"], "nmap -V")
    run_command(containers["victim"], "snort -V")

    # Uncomment this if you want to auto-clean
    # cleanup(containers)

if __name__ == "__main__":
    main()
