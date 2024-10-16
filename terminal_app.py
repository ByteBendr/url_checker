import requests
from bs4 import BeautifulSoup
import socket
import time
import colorama
from colorama import Fore, Style
from click import pause

colorama.init()

WHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
RED = Fore.LIGHTRED_EX + Style.BRIGHT
GREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
BLUE = Fore.LIGHTCYAN_EX + Style.BRIGHT
RESET = Style.RESET_ALL

def get_webpage_info(url):
    try:
        # Measure time to load page
        start_time = time.time()
        
        # Send request to URL
        response = requests.get(url)
        load_time = time.time() - start_time
        
        # Get status code
        status_code = response.status_code
        
        # Get webpage title (if HTML)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        
        # Extract domain name from URL and get IP address
        domain_name = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(domain_name)
        
        # Check if page is up or not
        is_up = status_code == 200

        return {
            "title": title,
            "status_code": status_code,
            "load_time": round(load_time, 2),
            "ip_address": ip_address,
            "is_up": is_up
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "is_up": False
        }

# Example usage
url = input(f"{WHITE}> Enter the URL:{GREEN} ")
info = get_webpage_info(url)
if "error" in info:
    print(f"\n{RED}> Error: {info['error']}{RESET}")
else:
    print(f"\n{WHITE}URL Status Checker v1.0")
    print(f"{WHITE}=============================================================================={RESET}")
    print(f"{WHITE}> Title       : {BLUE}{info['title']}{RESET}")
    print(f"{WHITE}> Status Code : {BLUE}{info['status_code']}{RESET}")
    print(f"{WHITE}> Load Time   : {BLUE}{info['load_time']} seconds{RESET}")
    print(f"{WHITE}> IP Address  : {BLUE}{info['ip_address']}{RESET}")
    print(f"{WHITE}> Is Page Up  : {BLUE}{'Yes' if info['is_up'] else 'No'}{RESET}")
    print(f"{WHITE}=============================================================================={RESET}")

pause(f"{WHITE}\n> Press any key to exit{RESET}")