import os
import whois
import subprocess
from colorama import Fore, Back, Style, init
from commands import wifi, network, security, utils

init(autoreset=True)  # Initialize colorama for Windows

def netutility_banner():
        print(Fore.BLUE + "                                                                                                       ")
        print(Fore.BLUE + "     ##### #     ##                    ##### /    ##               ###                                 ")
        print(Fore.BLUE + "  ######  /#    #### /              ######  /  #####           #    ###    #                           ")
        print(Fore.BLUE + " /#   /  / ##    ###/          #   /#   /  /     ##### #      ###    ##   ###     #                    ")
        print(Fore.BLUE + "/    /  /  ##    # #          ##  /    /  ##     # ## ##       #     ##    #     ##                    ")
        print(Fore.BLUE + "    /  /    ##   #            ##      /  ###     #    ##             ##          ##                    ")
        print(Fore.BLUE + "   ## ##    ##   #    /##   ######## ##   ##     #  ######## ###     ##  ###   ######## ##   ####      ")
        print(Fore.BLUE + "   ## ##     ##  #   / ### ########  ##   ##     # ########   ###    ##   ### ########   ##    ###  /  ")
        print(Fore.BLUE + "   ## ##     ##  #  /   ###   ##     ##   ##     #    ##       ##    ##    ##    ##      ##     ###/   ")
        print(Fore.BLUE + "   ## ##      ## # ##    ###  ##     ##   ##     #    ##       ##    ##    ##    ##      ##      ##    ")
        print(Fore.BLUE + "   ## ##      ## # ########   ##     ##   ##     #    ##       ##    ##    ##    ##      ##      ##    ")
        print(Fore.BLUE + "   #  ##       ### #######    ##      ##  ##     #    ##       ##    ##    ##    ##      ##      ##    ")
        print(Fore.BLUE + "      /        ### ##         ##       ## #      #    ##       ##    ##    ##    ##      ##      ##    ")
        print(Fore.BLUE + "  /##/          ## ####    /  ##        ###      /    ##       ##    ##    ##    ##      ##      ##    ")
        print(Fore.BLUE + " /  #####           ######/   ##         #######/     ##       ### / ### / ### / ##       #########    ")
        print(Fore.BLUE + "/     ##             #####     ##          ####        ##       ##/   ##/   ##/   ##        #### ###   ")
        print(Fore.BLUE + "#                                                                                                 ###  ")
        print(Fore.BLUE + " ##                                                                                        #####   ### ")
        print(Fore.BLUE + "                                                                                         /#######  /#  ")
        print(Fore.BLUE + "                                                                                        /      ###/    ")


def devName():

        print(Fore.RED + "   ___         ______   _               ")
        print(Fore.RED + "  / _ )__ __  / __/ /  (_)  _____ ___ _ ")
        print(Fore.RED + " / _  / // / _\ \/ _ \/ / |/ / _ `/  ' \ ")
        print(Fore.RED + "/____/\_, / /___/_//_/_/|___/\_,_/_/_/_/")
        print(Fore.RED + "     /___/                              ")
        

def clear_screen():
    os.system('cls')  # Windows-only clear screen command

def pause():
    input(Fore.YELLOW + "\nPress Enter to return to the menu...")

def log_event(event):
    with open("logs/netutility.log", "a") as log_file:
        log_file.write(event + "\n")
    print(Fore.CYAN + f"[LOGGED] {event}")

def main_menu():
    while True:
        clear_screen()
        netutility_banner()
        print(Fore.RED + "\nNetUtility Version 1.0")
        devName()
        #print(Fore.BLUE + "")
        print(Fore.GREEN + "\n1. WiFi Utilities")
        print(Fore.CYAN + "2. Network Tools")
        print(Fore.RED + "3. Security Tools")
        print(Fore.YELLOW + "4. System Utilities")
        print(Fore.MAGENTA + "5. Exit")
        choice = input(Fore.WHITE + "Enter your choice: ")
        
        if choice == "1":
            wifi_menu()
        elif choice == "2":
            network_menu()
        elif choice == "3":
            security_menu()
        elif choice == "4":
            utils_menu()
        elif choice == "5":
            print(Fore.MAGENTA + "Exiting NetUtility...")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")
            pause()

def wifi_menu():
    while True:
        clear_screen()
        print(Back.GREEN + Fore.BLACK + "\nWiFi Utilities")
        print(Fore.GREEN + "1. Show Saved Passwords")
        print(Fore.GREEN + "2. Scan for WiFi Networks")
        print(Fore.GREEN + "3. Show Current Network")
        print(Fore.GREEN + "4. Back to Main Menu")
        choice = input(Fore.WHITE + "Enter your choice: ")
        
        if choice == "1":
            wifi.show_saved_passwords()
        elif choice == "2":
            wifi.scan_networks()
        elif choice == "3":
            wifi.show_current_network()
        elif choice == "4":
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")
        pause()

def network_menu():
    while True:
        clear_screen()
        print(Back.CYAN + Fore.BLACK + "\nNetwork Tools")
        print(Fore.CYAN + "1. Test Internet Speed")
        print(Fore.CYAN + "2. Scan Local Devices")
        print(Fore.CYAN + "3. WHOIS Lookup")
        print(Fore.CYAN + "4. List Connected Devices")
        print(Fore.CYAN + "5. Back to Main Menu")
        choice = input(Fore.WHITE + "Enter your choice: ")
        
        if choice == "1":
            network.test_speed()
        elif choice == "2":
            network.scan_local_devices()
        elif choice == "3":
            network.whois_lookup()
        elif choice == "4":
            network.list_connected_devices()
        elif choice == "5":
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")
        pause()

def security_menu():
    while True:
        clear_screen()
        print(Back.RED + Fore.BLACK + "\nSecurity Tools")
        print(Fore.RED + "1. Detect ARP Spoofing")
        print(Fore.RED + "2. Deauthenticate Device (Block MAC)")
        print(Fore.RED + "3. Scan for Open Ports")
        print(Fore.RED + "4. Check Firewall Status")
        print(Fore.RED + "5. Monitor Network Traffic")
        print(Fore.RED + "6. Back to Main Menu")
        choice = input(Fore.WHITE + "Enter your choice: ")
        
        if choice == "1":
            security.arp_spoof_detector()
        elif choice == "2":
            security.deauthenticate_device()
        elif choice == "3":
            security.scan_open_ports()
        elif choice == "4":
            security.check_firewall_status()
        elif choice == "5":
            security.monitor_network_traffic()
        elif choice == "6":
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")
        pause()

def utils_menu():
    while True:
        clear_screen()
        print(Back.YELLOW + Fore.BLACK + "\nSystem Utilities")
        print(Fore.YELLOW + "1. Show System Info")
        print(Fore.YELLOW + "2. Check Disk Usage")
        print(Fore.YELLOW + "3. Check RAM Usage")
        print(Fore.YELLOW + "4. Check CPU Usage")
        print(Fore.YELLOW + "5. Show Running Processes")
        print(Fore.YELLOW + "6. Get Public IP Address")
        print(Fore.YELLOW + "7. Back to Main Menu")
        choice = input(Fore.WHITE + "Enter your choice: ")
        
        if choice == "1":
            utils.show_system_info()
        elif choice == "2":
            utils.check_disk_usage()
        elif choice == "3":
            utils.check_ram_usage()
        elif choice == "4":
            utils.check_cpu_usage()
        elif choice == "5":
            utils.show_running_processes()
        elif choice == "6":
            utils.get_public_ip()
        elif choice == "7":
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")
        pause()

if __name__ == "__main__":
    main_menu()
