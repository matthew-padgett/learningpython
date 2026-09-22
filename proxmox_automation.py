import os
from shutil import disk_usage

import urllib3
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI

# Suppress self-signed certificate warnings (useful for homelab situations)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

PROXMOX_HOST = os.getenv("PROXMOX_HOST")
PROXMOX_USER = os.getenv("PROXMOX_USER")
TOKEN_NAME = os.getenv("PROXMOX_TOKEN_NAME")
TOKEN_VALUE = os.getenv("PROXMOX_TOKEN_VALUE")

if not all([PROXMOX_HOST, PROXMOX_USER, TOKEN_NAME, TOKEN_VALUE]):
    raise ValueError("Missing one or more required variables in your .env file!")

proxmox = ProxmoxAPI(
    PROXMOX_HOST,
    user=PROXMOX_USER,
    token_name=TOKEN_NAME,
    token_value=TOKEN_VALUE,
    verify_ssl=False
)

NODE = os.getenv("PROXMOX_NODE") # I am only using one node, so I put it as an env variable.

containers = proxmox.nodes(NODE).lxc.get()

for container in containers:
    vmid = container.get("vmid")
    name = container.get("name", "Unnamed")

    cpu_usage = container.get("cpu", 0.0)
    cpu_percent = cpu_usage * 100

    memory_usage = container.get("mem", 0.0)
    max_memory = container.get("maxmem", 1)
    # memory_in_megabytes = memory_usage / (1024 ** 2)
    # max_memory_in_megabytes = max_memory / (1024 ** 2)
    memory_percent = (memory_usage / max_memory) * 100

    print(f"LXC {vmid} ({name}): {cpu_percent:.1f}% CPU, {memory_percent:.1f}% RAM")

vms = proxmox.nodes(NODE).qemu.get()
for vm in vms:
    vmid = vm.get("vmid")
    name = vm.get("name", "Unnamed")

    cpu_usage = vm.get("cpu", 0.0)
    cpu_percent = cpu_usage * 100

    memory_usage = vm.get("mem", 0.0)
    max_memory = vm.get("maxmem", 1)
    memory_percent = (memory_usage / max_memory) * 100

    print(f"QEMU {vmid} ({name}): {cpu_percent:.1f}% CPU, {memory_percent:.1f}% RAM")