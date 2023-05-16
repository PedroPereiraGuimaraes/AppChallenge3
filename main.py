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
        for F in (Home, Speed, Config):
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

        global nav, home, data, velocity, config, total, tipoTrafego, download, upload, others, ssdp, https, dns, apps, download_back, upload_back, configuracoes

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
        others = tk.PhotoImage(file="./img/others.png")
        ssdp = tk.PhotoImage(file="./img/ssdp.png")
        https = tk.PhotoImage(file="./img/https.png")
        dns = tk.PhotoImage(file="./img/dns.png")
        apps = tk.PhotoImage(file="./img/apps.png")
        download_back = tk.PhotoImage(file="./img/download_back.png")
        upload_back = tk.PhotoImage(file="./img/upload_back.png")
        configuracoes = tk.PhotoImage(file="./img/configuracoes.png")

        #NAVBAR
        tk.Label(self, image=nav, bd=0, bg='#FFFFFF').place(x=0, y=200)
        tk.Button(self, image=home, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Home")).place(x=10, y=270)
        tk.Button(self, image=velocity, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Speed")).place(x=10, y=355)
        tk.Button(self, image=config, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Config")).place(x=10, y=440)

        #TRAFEGO
        tk.Label(self, image=total, bd=0, bg='#FFFFFF').place(x=150, y=80)
        tk.Label(self, image=tipoTrafego, bd=0, bg='#FFFFFF').place(x=700, y=80)
        tk.Label(self, text="TOTAL DISPONIVEL", width=25, height=2, bd=0, bg='#9664FF', foreground="#FFFFFF", font=10).place( x=285, y=250)
        tk.Label(self, text="TOTAL USADO", width=25, height=2, bd=0, bg='#9664FF', foreground="#FFFFFF", font=10).place( x=285, y=420)
        #DOWNLOADS
        tk.Label(self, image=download, bd=0, bg='#5029A3').place( x=720, y=230)
        #UPLOADS
        tk.Label(self, image=upload, bd=0, bg='#5029A3').place( x=720, y=460)
        #DNS
        tk.Label(self, image=dns, bd=0, bg='#5029A3').place( x=920, y=230)
        #HTTPS
        tk.Label(self, image=https, bd=0, bg='#5029A3').place( x=920, y=460)
        #SSDP
        tk.Label(self, image=ssdp, bd=0, bg='#5029A3').place( x=1120, y=230)
        #OTHERS
        tk.Label(self, image=others, bd=0, bg='#5029A3').place( x=1120, y=460)

        #BARRAS DE PROGRESSO
        #TRAFEGO
        totalbar(self,x=300, y=300, max=40, value=30, len=200, color="#777777")
        progressbar(self,x=300, y=470, max=40, value=10, len=200, color="#A4CE48")
        #DOWNLOADS
        totalbar(self, x=740, y=310, max=40, value=30, len=140, color="#777777")
        progressbar(self, x=740, y=345, max=40, value=15, len=140, color="#A4CE48")
        #UPLOADS
        totalbar(self, x=740, y=550, max=40, value=30, len=140, color="#777777")
        progressbar(self, x=740, y=580, max=40, value=11, len=140, color="#A4CE48")
        #JOGOS
        totalbar(self, x=940, y=560, max=40, value=30, len=140, color="#777777")
        #STREAMING
        totalbar(self, x=940, y=330, max=40, value=30, len=140, color="#777777")
        #SOCIALS
        totalbar(self, x=1140, y=330, max=40, value=30, len=140, color="#777777")
        #OUTROS
        totalbar(self, x=1140, y=560, max=40, value=30, len=140, color="#777777")



class Speed(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#FFFFFF')

        #NAVBAR
        #NAVBAR
        tk.Label(self, image=nav, bd=0, bg='#FFFFFF').place(x=0, y=200)
        tk.Button(self, image=home, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Home")).place(x=10, y=270)
        tk.Button(self, image=velocity, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Speed")).place(x=10, y=355)
        tk.Button(self, image=config, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Config")).place(x=10, y=440)

        #DOWNLOAD E UPLOAD
        tk.Label(self, image=download_back, bd=0, bg='#FFFFFF').place(x=150, y=80)
        tk.Label(self, image=upload_back, bd=0, bg='#FFFFFF').place(x=800, y=80)

        tk.Label(self, text="TAXA DE DADOS", width=25, height=2, bd=0, bg='#9664FF', foreground="#FFFFFF", font=10).place( x=940, y=350)
        totalbar(self,x=955, y=400, max=40, value=30, len=200, color="#F95151", text="/s")

        tk.Label(self, text="TAXA DE DADOS", width=25, height=2, bd=0, bg='#9664FF', foreground="#FFFFFF", font=10).place( x=285, y=350)
        totalbar(self,x=300, y=400, max=40, value=30, len=200, color="#F95151", text="/s")
        
class Config(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#FFFFFF')
 
        #NAVBAR
        tk.Label(self, image=nav, bd=0, bg='#FFFFFF').place(x=0, y=200)
        tk.Button(self, image=home, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Home")).place(x=10, y=270)
        tk.Button(self, image=velocity, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Speed")).place(x=10, y=355)
        tk.Button(self, image=config, bd=0, bg="#9664FF", activebackground='#9664FF', command=lambda:controller.show_frame("Config")).place(x=10, y=440)

        #CONFIGURACAO
        tk.Label(self, image=configuracoes, bd=0, bg='#FFFFFF').place(x=150, y=80)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()