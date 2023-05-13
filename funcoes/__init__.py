import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def grafico(x,y,tot,usg):
    plt.close('all')
    fig, ax = plt.subplots(figsize=(1.4, 1.4)) # aumenta o tamanho da figura para exibir a pizza
    sizes = [tot, usg]
    colors = ['#5029A3', '#A4CE48']
    nomes = ["Total", "Usado"]
    ax.pie(sizes, labels=nomes, colors=colors, autopct='%1.1f%%', textprops={'color': 'white'}) # usa a função "pie" para criar o gráfico de pizza
    ax.set_facecolor('#9664FF')
    fig.set_facecolor('#9664FF')

    canvas = FigureCanvasTkAgg(fig)
    canvas.get_tk_widget().place(x=x, y=y)


def grafico2(x,y,tot,usg):
    plt.close('all')
    fig, ax = plt.subplots(figsize=(4, 4)) # aumenta o tamanho da figura para exibir a pizza
    sizes = [tot, usg]
    colors = ['#9664FF', '#A4CE48']
    nomes = ["Total para uso", "Total usado"]
    ax.pie(sizes, labels=nomes, colors=colors, autopct='%1.1f%%', textprops={'color': 'white', 'fontsize': 10}) # usa a função "pie" para criar o gráfico de pizza
    ax.set_facecolor('#5029A3')
    fig.set_facecolor('#5029A3')

    canvas = FigureCanvasTkAgg(fig)
    canvas.get_tk_widget().place(x=x, y=y)



def handle_socket_connection(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', port))
            print(f'Connected to port {port}.')

            while True:
                data = s.recv(1024)
                if not data:
                    break
                print(f'Received from port {port}: {data.decode()}')
    except Exception as e:
        print(f'Error in connection to port {port}: {e}')


def futures():
    try:
        futures = []
        futures.append(handle_socket_connection(50000))
        for future in futures:
            future
    except Exception as e:
        print(f'Error: {e}')
