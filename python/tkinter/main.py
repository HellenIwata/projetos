from tkinter import *
from tkinter import ttk

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.create_config_screen()
        self.create_frames_screen()
        self.create_widgets_primary_frame()
        self.create_list_secundary_frame()        
        
        root.mainloop()
    
    ##Definindo as configurações da tela
    def create_config_screen(self):
        self.root.wm_title('Cadastro de cliente') # Define o titulo na janela da tela
        self.root.configure(background='#00334d') # Define a cor de fundo da janela
        self.root.wm_geometry('700x5000') # Define a geometria da janela (largura x altura)
        self.root.wm_resizable(True, True) # Define que a janela será responsiva, em caso de 'False, False' significa que a janela não será responsiva.
        self.root.wm_maxsize(width=900, height=700) # Define as dimensões máximas permitidas para redimensionar a janela
        self.root.wm_minsize(width=600, height=700) # Define o tamanho minimo permitido para redimensionar a janela
    
    ##Defindo quantidades de frames, tamanhos e estilos
    def create_frames_screen(self):
        self.primary_frame = Frame(self.root, bg='#dfe5ec', border=3, highlightbackground= '#e6f7ff', 
                                highlightthickness=4)
        self.primary_frame.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.35) # relx = define onde o frame terá inicio(espaçamento a esquerda)/rely define onde o frame irá terminar (espaçamento a direita)
        
        self.secundary_frame = Frame(self.root, bd=4, bg='#dfe5ec',
                            highlightbackground='#e6f7ff', highlightthickness=4)
        self.secundary_frame.place(relx=0.02, rely=0.40, relwidth=0.96, relheight=0.56)
    
    ## Criando e definindo estilos dos widgets da tela principal
    def create_widgets_primary_frame(self):
        #Criação do botão 'limpar'
        self.btn_clear = Button(self.primary_frame, text='Limpar', 
                            border=5, bg='#00334d', fg='#fff', font=('verdana', 8, 'bold')).place(
                            relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
        #Criação do botão 'buscar'
        self.btn_buscar = Button(self.primary_frame, text='Buscar',
                                border=5, bg='#00334d', fg='#fff', font=('verdana', 8, 'bold')).place(
                                relx=0.305, rely=0.1, relwidth=0.1, relheight=0.1)
    
        #Criação do botão 'novo'
        self.btn_new = Button(self.primary_frame, text='Novo',
                                border=5, bg='#00334d', fg='#fff', font=('verdana', 8, 'bold')).place(
                                relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)
    
        #Criação do botão 'alterar'
        self.btn_alter = Button(self.primary_frame, text='Alterar',
                                border=5, bg='#00334d', fg='#fff', font=('verdana', 8, 'bold')).place(
                                relx=0.705, rely=0.1, relwidth=0.1, relheight=0.1)
    
        #Criação do botão 'apagar'
        self.btn_del = Button(self.primary_frame, text='Apagar',
                            border=5, bg='#00334d', fg='#fff', font=('verdana', 8, 'bold')).place(
                            relx=0.81, rely=0.1, relwidth=0.1, relheight=0.1)
    
        #Criação das 'Labels' e 'Entrys' para os dados do cliente
        self.lb_code = Label(self.primary_frame, text='Código', bg='#dfe5ec', fg='#00334d', font=('verdana', 9, 'bold')).place(relx=0.05, rely=0.04)
        self.entry_code = Entry(self.primary_frame, bg='#cfd8e2').place(relx=0.05, rely=0.12, relwidth=0.08)
        
        self.lb_name = Label(self.primary_frame, text='Nome', bg='#dfe5ec', fg='#00334d', font=('verdana', 9, 'bold')).place(relx=0.05, rely=0.32)
        self.entry_nome = Entry(self.primary_frame, bg='#cfd8e2').place(relx=0.05, rely=0.405, relwidth=0.8)
        
        self.lb_phone = Label(self.primary_frame, text='Telefone', bg='#dfe5ec', fg='#00334d', font=('verdana', 9, 'bold')).place(relx=0.05, rely=0.60)
        self.entry_phone = Entry(self.primary_frame, bg='#cfd8e2').place(relx=0.05, rely=0.685, relwidth=0.35)
        
        self.lb_city = Label(self.primary_frame, text='Cidade', bg='#dfe5ec', fg='#00334d', font=('verdana', 9, 'bold')).place(relx=0.5, rely=0.60)
        self.entry_city = Entry(self.primary_frame, bg='#cfd8e2').place(relx=0.5, rely=0.685, relwidth=0.35)
        
        
    def create_list_secundary_frame(self):        
        self.client_list = ttk.Treeview(self.secundary_frame, height=3,columns=('col1', 'col2', 'col3', 'col4'))
        
        self.client_list.heading("#0", text="")
        self.client_list.heading("#1", text="ID")
        self.client_list.heading("#2", text="Nome")
        self.client_list.heading("#3", text="Telefone")
        self.client_list.heading("#4", text="Cidade")
        
        self.client_list.column("#0", width=1)
        self.client_list.column("#1", width=50)
        self.client_list.column("#2", width=230)
        self.client_list.column("#3", width=125)
        self.client_list.column("#4", width=210)
        self.client_list.place(relx=0.01, rely=0.05, relwidth=0.965, relheight=0.90)
        
        
        
        """ self.scroolLista = Scrollbar(self.client_list, orient='vertical')
        self.client_list.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.958, rely=0.005, relwidth=0.04, relheight=0.975) """

Application()