import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def grafico(x,y,tot,usg):
    plt.close('all')
    fig, ax = plt.subplots(figsize=(1.6, 1))
    ax.barh(0, tot, align='center', height=.5, color='#000000')
    ax.barh(1, usg, align='center', height=.5, color='#5029A3')
    ax.invert_yaxis()
    nomes = ["ToT", "Usg"]
    for i, nome in enumerate(nomes):
        ax.text(0, i, nome, ha="right", va="center", fontsize=8, color="white")
    ax.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
    ax.set_facecolor('#9664FF')
    fig.set_facecolor('#9664FF')

    canvas = FigureCanvasTkAgg(fig)
    canvas.get_tk_widget().place(x=x, y=y)

