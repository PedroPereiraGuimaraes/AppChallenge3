from tkinter import *
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

def createPieChart(self, PieV, colV, x, y):
    canvas = Canvas(self,width=140,height=140,bg='#9664FF',highlightbackground='#9664FF')
    canvas.place(x=x,y=y)
    st = 0
    coord = 0, 0, 140, 140
    for val,col in zip(PieV,colV):    
        canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
        st = st + val*3.6 


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

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', port))

            while True:
                data = s.recv(500000)
                if not data:
                    break
                data_received = data.decode()[1:].replace('\\','').replace('\n','').replace("'",'')
                json_data = json.loads(data_received)
                return json_data
                        
    except Exception as e:
        print(f'Error in connection to port {port}: {e}')
