import os
import subprocess
from commands.utils import pause

def arp_spoof_detector():
    print("Checking for ARP spoofing...")
    os.system("arp -a")
    pause()

def deauthenticate_device():
    target_mac = input("Enter target MAC address: ")
    print(f"Blocking device {target_mac} from connecting to the network...")
    os.system(f'netsh wlan add filter permission=block mac={target_mac}')
    print("Device blocked successfully.")
    pause()

def scan_open_ports():
    target_ip = input("Enter IP to scan for open ports: ")
    print(f"Scanning open ports on {target_ip}...")
    os.system(f"netstat -an | findstr {target_ip}")
    pause()

def check_firewall_status():
    print("Checking Windows Firewall status...")
    os.system("netsh advfirewall show allprofiles")
    pause()

def monitor_network_traffic():
    print("Monitoring active network connections...")
    os.system("netstat -an")
    pause()