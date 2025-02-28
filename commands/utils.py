import os
import requests
import psutil
from colorama import Fore, Back, Style, init

init(autoreset=True) 


def log_event(event):
    with open("logs/netutility.log", "a") as log_file:
        log_file.write(event + "\n")
    print(f"[LOGGED] {event}")

def format_output(title, data):
    print("=" * 40)
    print(f"{title.upper()}")
    print("=" * 40)
    print(data)
    print("=" * 40)

def show_system_info():
    print(Fore.YELLOW + "System Information:")
    print(Fore.CYAN + f"OS: {os.name}")
    print(Fore.CYAN + f"CPU Count: {psutil.cpu_count(logical=True)}")
    print(Fore.CYAN + f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    pause()

def check_disk_usage():
    usage = psutil.disk_usage('/')
    print(Fore.YELLOW + f"Disk Usage: {usage.percent}%")
    pause()

def check_ram_usage():
    usage = psutil.virtual_memory()
    print(Fore.YELLOW + f"RAM Usage: {usage.percent}%")
    pause()

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    print(Fore.YELLOW + f"CPU Usage: {usage}%")
    pause()

def show_running_processes():
    print(Fore.YELLOW + "Running Processes:")
    for proc in psutil.process_iter(['pid', 'name']):
        print(Fore.CYAN + f"PID: {proc.info['pid']} - Name: {proc.info['name']}")
    pause()

def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=text")
        print(Fore.YELLOW + f"Public IP Address: {response.text}")
    except Exception as e:
        print(Fore.RED + f"Error fetching public IP: {e}")
    pause()

def pause():
    input("\nPress Enter to return to the menu...")

