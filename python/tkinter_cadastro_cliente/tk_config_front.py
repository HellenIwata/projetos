from tkinter import *
from tkinter import ttk 

from config_back.config_btn_frame_top import Create_functions_btn
from config_back.config_db import Config_sqlite

class Frontend_configuaration_frame(Create_functions_btn, Config_sqlite):
    def __init__(self):
        self.window = Tk()
        # self.style = ttk.Style()
        self.create_config_window()
        self.create_frame_window()
        self.create_widgets_frame_top()
        self.create_list_frame_button()
        self.create_tb_client()
        self.select_client_list()
        self.header()
        
        self.window.mainloop()
    
    def header(self):
        '''Função responsável por configurar o menu superior da aplicação'''
        
        menu_bar = Menu(self.window)
        self.window.configure(menu=menu_bar)
        
        #Necessário criar uma variável para cada menu que deseja adicionar
        file_menu = Menu(menu_bar, tearoff=0)
        option_menu = Menu(menu_bar, tearoff=0)
        help_menu = Menu(menu_bar, tearoff=0)
        #sub_menu = Menu(option_menu, tearoff=0) #Opção para adicionar um submenu

        #Com o .add_cascade > Se cria o nome de cada menu principal
        #Com o .add_command > Se cria os comandos e os menus secundarios de cada menu
        menu_bar.add_cascade(label="Arquivo", underline=0, menu=file_menu) #Criando o Menu
        file_menu.add_command(label='Sair', command=self.window.destroy) #Criando as opções dentro do menu
        
        menu_bar.add_cascade(label='Opções', underline=0, menu=option_menu)
        option_menu.add_command(label='Limpar Campos', command=self.clear_screen)
        #Adicionando o SubMenu no menu opções
        #sub_menu.add_command(label='')
        
        menu_bar.add_cascade(label='Ajuda', underline=0, menu=help_menu)
        help_menu.add_command(label='Bem-Vindo')
        help_menu.add_command(label='About...')
    
    def create_config_window(self):
        '''Criação da configurações da janela'''
        #Titulo da Janela
        self.window.wm_title('Cadastro de cliente')
        #Cor de fundo da janela
        self.window.configure(bg='#19334d')
        #Tamanho padrão que a janela irá abrir ao chamar a aplicação
        self.window.wm_geometry('700x600')
        #Define a responsividade da janela,em caso de 'False' a janela não será responsiva
        self.window.wm_resizable(True, True)
        #Tamanho máximo que a tela  pode ter para o usuario redimensionar 
        self.window.wm_maxsize(width=900, height=700)
        self.window.wm_minsize(width=500, height=400)
    
    def create_frame_window(self):
        ''' Criação dos frames onde os widgets ficam '''
        
        #Estilo, tamanho e posição do primeiro frame
        self.frame_top = Frame(self.window, bg='#C2D1F0', border=3, highlightbackground='#3366CC',highlightthickness=4)
        self.frame_top.place(relx=0.02, rely=0.025, relwidth=0.96, relheight=0.45)
        
        #Estilo, tamanho e posição do primeiro frame
        self.frame_button = Frame(self.window, bg='#C2D1F0', border=3, highlightbackground='#3366CC',highlightthickness=4)
        self.frame_button.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.475)
    
    def create_widgets_frame_top(self):
        ''' Criação dos botões, labels e entrys do primeiro frame: frame_top '''
        
        #Definindo os BOTÕES
        
        ##Botão BUSCAR
        self.btn_search = Button(self.frame_top, text='BUSCAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'))
        self.btn_search.place(relx=0.2, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão LIMPAR
        self.btn_clear = Button(self.frame_top, text='LIMPAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'), 
            command=self.clear_screen)
        self.btn_clear.place(relx=0.305, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão ALTERAR
        self.btn_alter = Button(self.frame_top, text='ALTERAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'),
            command=self.client_alter)
        self.btn_alter.place(relx=0.705, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão EXCLUIR
        self.btn_del = Button(self.frame_top, text='EXCLUIR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'),
            command=self.client_delete)
        self.btn_del.place(relx=0.81, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão CADASTRAR
        self.btn_register = Button(self.frame_top, text='CADASTRAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'),
            command=self.add_client)
        self.btn_register.place(relx=0.815, rely=0.85, relwidth=0.12, relheight=0.1)
        
        #Definindo as Labels e Entrys
        
        ##Label CÓDIGO
        self.lb_code = Label(self.frame_top, text='CÓDIGO', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_code.place(relx=0.03, rely=0.05)
        
        ##Entry CODIGO
        self.ent_code = Entry(self.frame_top, bg='#eaf0fa', font=("Arial", 8))
        self.ent_code.place(relx=0.03, rely=0.15, relwidth=0.1)
        
        
        ##Label NOME
        self.lb_name = Label(self.frame_top, text='NOME', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_name.place(relx=0.03, rely=0.30)
        
        ##Entry NOME
        self.ent_name = Entry(self.frame_top, bg='#eaf0fa', font=("Arial", 8))
        self.ent_name.place(relx=0.03, rely=0.4, relwidth=0.88)
        
        
        ##Label TELEFONE
        self.lb_phone = Label(self.frame_top, text='TELEFONE', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_phone.place(relx=0.03, rely=0.55)
        
        ##Entry TELEFONE
        self.ent_phone = Entry(self.frame_top, bg='#eaf0fa', font=("Arial", 8))
        self.ent_phone.place(relx=0.03, rely=0.65, relwidth=0.20)
        
        
        ##Label E-MAIL
        self.lb_email = Label(self.frame_top, text='E-MAIL', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_email.place(relx=0.3, rely=0.55)
        
        ##Entry E-MAIL
        self.ent_email = Entry(self.frame_top, bg='#eaf0fa', font=("Arial", 8))
        self.ent_email.place(relx=0.3, rely=0.65, relwidth=0.25)
        
        
        ##Label CIDADE
        self.lb_city = Label(self.frame_top, text='CIDADE', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_city.place(relx=0.65, rely=0.55)
        
        ##Entry CIDADE
        self.ent_city = Entry(self.frame_top, bg='#eaf0fa', font=("Arial", 8))
        self.ent_city.place(relx=0.65, rely=0.65, relwidth=0.255)    
        
    def create_list_frame_button(self):
        '''Cria o frame inferior que contem a lista de clientes'''
        
        self.client_list = ttk.Treeview(self.frame_button, displaycolumns=(1,2,3,4,5), columns=(1,2,3,4,5),
                                        show='headings', selectmode='extended', padding=10)        
        #Cabeçalho da tabela
        # self.client_list.heading(0, text=' ')
        self.client_list.heading(1, text='ID')
        self.client_list.heading(2, text= 'NOME')
        self.client_list.heading(3, text= 'TELEFONE')
        self.client_list.heading(4, text='EMAIL')
        self.client_list.heading(5, text='CIDADE')
        
        # self.client_list.column(0, anchor='w', width=50)
        self.client_list.column(1, anchor='center', width=10)
        self.client_list.column(2, anchor='center', width=150) 
        self.client_list.column(3, anchor='center', width=75)   
        self.client_list.column(4, anchor='center', width=150)
        self.client_list.column(5, anchor='center', width=55)
        
        # self.client_list.insert('', 'end', iid=1, values=(1,'Hellen Cristina','11930889923','hiwata001@icloud.com','SP'))
        
        self.client_list.place(relx=0.02, rely=0.02, relwidth=0.97, relheight=0.94)
        
        self.client_list.bind('<Double-1>', self.on_double_click)
        
    

Frontend_configuaration_frame()