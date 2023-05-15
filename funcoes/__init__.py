import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import socket
import json
from tkinter import ttk

def progressbar(self, x, y, max, value, len, color):

    style = ttk.Style()
    style.theme_use('default')
    style.configure("blue.Horizontal.TProgressbar", foreground='none', background=color, troughcolor='#FFFFFF', bordercolor='#FFFFFF')
    style.configure("CustomLabel.TLabel", foreground='black', background='#FFFFFF')


    progressbar = ttk.Progressbar(self, orient="horizontal", length=len, mode="determinate", style="blue.Horizontal.TProgressbar")
    progressbar.place(x=x,y=y)

    label = ttk.Label(self, text="", style="CustomLabel.TLabel")
    label.place(x=x+2, y=y+2)

    progressbar["maximum"] = max
    progressbar["value"] = value
    label["text"] = str(progressbar["value"]), "GB"

def totalbar(self, x, y, max, value, len, color, text=""):

    style = ttk.Style()
    style.theme_use('default')
    style.configure("green.Horizontal.TProgressbar", foreground='none', background=color, troughcolor='#FFFFFF', bordercolor='#FFFFFF')
    style.configure("CustomLabel.TLabel", foreground='black', background='#FFFFFF')


    progressbar = ttk.Progressbar(self, orient="horizontal", length=len, mode="determinate", style="green.Horizontal.TProgressbar")
    progressbar.place(x=x,y=y)

    label = ttk.Label(self, text="", style="CustomLabel.TLabel")
    label.place(x=x+2, y=y+2)

    progressbar["maximum"] = max
    progressbar["value"] = value
    label["text"] = str(progressbar["value"]), f"GB{text}"


def handle_socket_connection(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', port))

            while True:
                data = s.recv(500000)
                if not data:
                    break
                data_received = data.decode()[1:].replace('\\','').replace('\n','').replace("'",'')
                print(data_received, "\n")
                json_data = json.loads(data_received)

                for pid in json_data:
                        pid_data = json_data[pid]
                        print(f"PID: {pid}")
                        print(f"Name: {pid_data['name']}")
                        print(f"Create Time: {pid_data['create_Time']}")
                        print(f"Last Time Updated: {pid_data['last_time_updated']}")
                        print(f"Upload: {pid_data['upload']}")
                        print(f"Download: {pid_data['download']}")
                        print(f"Upload Speed: {pid_data['upload_speed']}")
                        print(f"Download Speed: {pid_data['download_speed']} \n")

    except Exception as e:
        print(f'Error in connection to port {port}: {e}')