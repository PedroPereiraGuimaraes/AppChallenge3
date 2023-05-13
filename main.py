import tkinter as tk
from tkinter import font as tkfont
from funcoes import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Righteous', size=18)
        self.base_font = tkfont.Font(family='Righteous', size=13)
        self.title("AppChallenge")
        self.iconbitmap("./img/viasat.ico")

        width_janela = 1366
        height_janela = 768
        width_tela = self.winfo_screenwidth()
        height_tela = self.winfo_screenheight()
        pos_x = int((width_tela - width_janela) / 2)
        pos_y = int((height_tela - height_janela) / 2)

        self.geometry("{}x{}+{}+{}".format(width_janela, height_janela, pos_x, pos_y))

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        
        

        self.frames = {}
        for F in (Home, Dados, Speed, Config):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Home(tk.Frame):

    def __init__(self, parent, controller):

        global nav, home, data, velocity, config, total, tipoTrafego, download, upload, jogos, streaming, socials, outros

        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.attributes()
        self.configure(bg='#FFFFFF')

        #IMPORTANDO AS IMAGENS
        nav = tk.PhotoImage(file="./img/nav.png")
        home = tk.PhotoImage(file="./img/home.png")
        data = tk.PhotoImage(file="./img/data.png")
        velocity = tk.PhotoImage(file="./img/velocity.png")
        config = tk.PhotoImage(file="./img/config.png")
        total = tk.PhotoImage(file="./img/total.png")
        tipoTrafego = tk.PhotoImage(file="./img/tipoTrafego.png")
        download = tk.PhotoImage(file="./img/download.png")
        upload = tk.PhotoImage(file="./img/upload.png")
        jogos = tk.PhotoImage(file="./img/jogos.png")
        streaming = tk.PhotoImage(file="./img/streaming.png")
        socials = tk.PhotoImage(file="./img/socials.png")
        outros = tk.PhotoImage(file="./img/outros.png")

        #NAVBAR
        tk.Label(self, image=nav, bd=0, bg='#FFFFFF').place(x=0, y=200)
        tk.Button(self, image=home, bd=0, bg="#9664FF", activebackground='#9664FF').place(x=10, y=245)
        tk.Button(self, image=data, bd=0, bg="#9664FF", activebackground='#9664FF').place(x=10, y=320)
        tk.Button(self, image=velocity, bd=0, bg="#9664FF", activebackground='#9664FF').place(x=10, y=395)
        tk.Button(self, image=config, bd=0, bg="#9664FF", activebackground='#9664FF').place(x=10, y=470)


        #TRAFEGO
        tk.Label(self, image=total, bd=0, bg='#FFFFFF').place(x=150, y=80)
        tk.Label(self, image=tipoTrafego, bd=0, bg='#FFFFFF').place(x=700, y=80)

        #DOWNLOADS
        tk.Label(self, image=download, bd=0, bg='#5029A3').place( x=720, y=230)
        grafico(730,300,300,200)
        #UPLOADS
        tk.Label(self, image=upload, bd=0, bg='#5029A3').place( x=720, y=460)
        grafico(730,530,300,200)
        #JOGOS
        tk.Label(self, image=jogos, bd=0, bg='#5029A3').place( x=920, y=230)
        grafico(930,300,300,200)
        #STREAMING
        tk.Label(self, image=streaming, bd=0, bg='#5029A3').place( x=920, y=460)
        grafico(930,530,300,200)
        #SOCIALS
        tk.Label(self, image=socials, bd=0, bg='#5029A3').place( x=1120, y=230)
        grafico(1130,300,300,200)
        #OUTROS
        tk.Label(self, image=outros, bd=0, bg='#5029A3').place( x=1120, y=460)
        grafico(1130,530,300,200)


class Dados(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#FFFFFF')


class Speed(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#FFFFFF')
        
class Config(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#FFFFFF')

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()