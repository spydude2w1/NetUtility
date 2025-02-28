import os
from commands.utils import pause


def show_saved_passwords():
    print("Fetching saved WiFi passwords...")
    os.system("netsh wlan show profiles")
    pause()

def scan_networks():
    print("Scanning for available WiFi networks...")
    os.system("netsh wlan show networks")
    pause()

def show_current_network():
    print("Displaying current WiFi network...")
    os.system("netsh wlan show interfaces")
    pause()