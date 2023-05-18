from tkinter import *
import socket
import json
import re
import subprocess
import threading
from tkinter import messagebox
from apscheduler.schedulers.background import BackgroundScheduler

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


def graficos(self):
    data = handle_socket_connection(50001)
    if data != None:
        #TRAFEGO
        total = 500
        trafego = (data['total']/(total+0.000000000000000000000000000001))*100
        if data['total']/total <= 1:
            createPieChart(self,[100-trafego, trafego],["#1C064A","#A4CE48"],310,310,200,200)
        #DOWNLOADS
        download = (data['download']/(data['total']+0.00000000000000000000000001))*100
        if download <= 1:
            createPieChart(self,[99.99, 0.01],["#B431B8","#A4CE48"],740,280,140,140)
        else:
            createPieChart(self,[100-download, download],["#A4CE48","#B431B8"],740,280,140,140)
        #UPLOADS
        upload = (data['upload']/(data['total']+0.00000000000000000000000001))*100
        if upload <= 1:
            createPieChart(self,[99.99, 0.01],["#B431B8","#A4CE48"],740,510,140,140)
        else:
            createPieChart(self,[100-upload, upload],["#A4CE48","#B431B8"],740,510,140,140)
        #DNS
        dns = (data['domain']/(data['total']+0.00000000000000000000000001))*100
        if dns <= 5:
            createPieChart(self,[99.99, 0.01],["#B431B8","#A4CE48"],940,280,140,140)
        else:
            createPieChart(self,[100-dns, dns],["#A4CE48","#B431B8"],940,280,140,140)
        #HTTPS
        https = (data['https']/(data['total']+0.00000000000000000000000001))*100
        if https <= 5:
            createPieChart(self,[99.99, 0.01],["#B431B8","#A4CE48"],940,510,140,140)
        else:
            createPieChart(self,[100-https, https],["#A4CE48","#B431B8"],940,510,140,140)
        #SSDP
        ssdp = (data['ssdp']/(data['total']+0.00000000000000000000000001))*100
        if ssdp <= 5:
            createPieChart(self,[99.99, 0.01],["#B431B8","#A4CE48"],1140,280,140,140)
        else:
            createPieChart(self,[100-ssdp, ssdp],["#A4CE48","#B431B8"],1140,280,140,140)
        #OTHERS
        others = (data['others']/(data['total']+0.00000000000000000000000001))*100
        if others <= 5:
            createPieChart(self,[99.99, 0.01],["#B431B8","#A4CE48"],1140,510,140,140)
        else:
            createPieChart(self,[100-others, others],["#A4CE48","#B431B8"],1140,510,140,140)
    else:
        messagebox.showinfo("Erro", "Habilite o package tracer ou espere a chegada de dados.")

def createPieChart(self, PieV, colV, x, y, width, height):
    if hasattr(self, 'canvas'):
        self.canvas.destroy()

    canvas = Canvas(self,width=width,height=height,bg='#FFFFFF',highlightbackground='#FFFFFF')
    canvas.place(x=x,y=y)
    st = 0
    coord = 0, 0, width, height
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
                https=domain =ssdp=others=download=upload =0
                try:
                    download += convert_size_to_bytes(json_data["https"]["download"])
                except:
                    download += 0

                try:
                    download += convert_size_to_bytes(json_data["domain"]["download"])
                except:
                    download += 0

                try:
                    download += convert_size_to_bytes(json_data["ssdp"]["download"])
                except:
                    download += 0

                try:
                    download += convert_size_to_bytes(json_data["others"]["download"])
                except:
                    download += 0

                try:
                    upload += convert_size_to_bytes(json_data["https"]["upload"])
                except:
                    upload += 0

                try:
                    upload += convert_size_to_bytes(json_data["domain"]["upload"])
                except:
                    upload += 0
                
                try:
                    upload += convert_size_to_bytes(json_data["ssdp"]["upload"])
                except:
                    upload += 0
                
                try:
                    upload += convert_size_to_bytes(json_data["others"]["upload"])
                except:
                    upload += 0

                try:
                    https = convert_size_to_bytes(json_data["https"]["total"])
                except:
                    https += 0

                try:
                    domain = convert_size_to_bytes(json_data["domain"]["total"])
                except:
                    domain += 0

                try:
                    ssdp =  convert_size_to_bytes(json_data["ssdp"]["total"])
                except:
                    ssdp += 0

                try:
                    others = convert_size_to_bytes(json_data["others"]["total"])
                except:
                    others += 0

                values = {
                    'https': round(https,3),
                    'domain': round(domain,3),
                    'ssdp': round(ssdp,3),
                    'others': round(others,3),
                    'upload': round(upload,3),
                    'download': round(download,3),
                    'total': round(round(download,3)+round(upload,3),3)
                }

                return values
            
    except Exception as e:
        print(f"Erro na porta{e}")