import os
import whois
import subprocess
from commands.utils import pause



def test_speed():
    print("Testing internet speed...")
    os.system("speedtest-cli")
    pause()

def scan_local_devices():
    print("Scanning local network devices...")
    os.system("arp -a")
    pause()


def whois_lookup():
    domain = input("Enter domain/IP: ")
    print(f"Performing WHOIS lookup for {domain}...\n")
    try:
        result = whois.whois(domain)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    pause()


def list_connected_devices():
    print("Fetching connected devices...\n")
    result = subprocess.run("arp -a", shell=True, capture_output=True, text=True)

    if result.stdout:
        print(result.stdout)
    else:
        print("No connected devices found.")

    pause()

