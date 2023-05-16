from tkinter import ttk
import socket
import json
import re
import subprocess
import threading

def run():

    def executar_programa1():
        subprocess.run(['python', "./funcoes/traffic_analyzer.py"])
    
    def executar_programa2():
        subprocess.run(['python', './main.py'])
    
    # Cria as threads para executar os programas
    thread1 = threading.Thread(target=executar_programa1)
    thread2 = threading.Thread(target=executar_programa2)
    
    # Inicia as threads
    thread1.start()
    thread2.start()
    
    # Aguarda as threads terminarem
    thread1.join()
    thread2.join()

    print("Programas finalizados.")


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



def convert_size_to_bytes(size_str):
    size_str = size_str.upper()
    units = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4, "PB": 1024**5}
    pattern = re.compile(r'(\d*\.?\d+)([a-zA-Z]+)')
    match = pattern.match(size_str)

    if not match:
        raise ValueError("Tamanho inválido")

    size = float(match.group(1))
    unit = match.group(2)

    if unit not in units:
        raise ValueError("Unidade inválida")

    return float((size * units[unit])/1024**2)


def handle_socket_connection(port):

    total = 0
    https_down = 0
    https_up = 0
    dns_down = 0
    dns_up = 0
    ssdp_up = 0
    ssdp_down = 0
    others_up = 0
    others_down = 0

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', port))

            while True:
                data = s.recv(500000)
                if not data:
                    break
                data_received = data.decode()[1:].replace('\\', '').replace('\n', '').replace("'", '')
                json_data = json.loads(data_received)

                for pid in json_data:
                    pid_data = json_data[pid]
                    total += convert_size_to_bytes(pid_data["total"])
                    if pid == "others":
                        others_down += round(convert_size_to_bytes(pid_data["download"]),3)
                        others_up += round(convert_size_to_bytes(pid_data["upload"]),3)
                    elif pid == "https":
                        https_down += round(convert_size_to_bytes(pid_data["download"]),3)
                        https_up += round(convert_size_to_bytes(pid_data["upload"]),3)
                    elif pid == "domain":
                        dns_down += round(convert_size_to_bytes(pid_data["download"]),3)
                        dns_up += round(convert_size_to_bytes(pid_data["upload"]),3)
                    else:
                        ssdp_down += round(convert_size_to_bytes(pid_data["download"]),3)
                        ssdp_up += round(convert_size_to_bytes(pid_data["upload"]),3)
                        
                    yield others_down, others_up, https_down, https_up, dns_down, dns_up, ssdp_down, ssdp_up

    except Exception as e:
        print(f'Error in connection to port {port}: {e}')
