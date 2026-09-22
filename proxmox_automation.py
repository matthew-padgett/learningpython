import os
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

print(proxmox("nodes").get())