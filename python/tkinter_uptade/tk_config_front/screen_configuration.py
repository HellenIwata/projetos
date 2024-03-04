from tkinter import *

class Frontend_configuaration_frame():
    def __init__(self):
        self.window = Tk()
        
        self.create_config_window()
        self.create_frame_window()
        self.create_widgets_frame_top()
        
        
        
        self.window.mainloop()
        
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
        
        ##Botão NOVO
        self.btn_new = Button(self.frame_top, text='NOVO', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'))
        self.btn_new.place(relx=0.2, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão BUSCAR
        self.btn_search = Button(self.frame_top, text='BUSCAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'))
        self.btn_search.place(relx=0.305, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão LIMPAR
        self.btn_clear = Button(self.frame_top, text='LIMPAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'))
        self.btn_clear.place(relx=0.6, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão ALTERAR
        self.btn_alter = Button(self.frame_top, text='ALTERAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'))
        self.btn_alter.place(relx=0.705, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão EXCLUIR
        self.btn_del = Button(self.frame_top, text='EXCLUIR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'))
        self.btn_del.place(relx=0.81, rely=0.12, relwidth=0.1, relheight=0.1)
        
        ##Botão CADASTRAR
        self.btn_register = Button(self.frame_top, text='CADASTRAR', border=5, bg='#142952', fg='#FFF', font=('Corbel',8,'bold'))
        self.btn_register.place(relx=0.815, rely=0.85, relwidth=0.12, relheight=0.1)
        
        #Definindo as Labels e Entrys
        
        ##Label CÓDIGO
        self.lb_code = Label(self.frame_top, text='CÓDIGO', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_code.place(relx=0.03, rely=0.05)
        
        ##Label NOME
        self.lb_name = Label(self.frame_top, text='NOME', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_name.place(relx=0.03, rely=0.30)
        
        ##Label TELEFONE
        self.lb_phone = Label(self.frame_top, text='TELEFONE', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_phone.place(relx=0.03, rely=0.60)
        
        ##Label E-MAIL
        self.lb_email = Label(self.frame_top, text='E-MAIL', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_email.place(relx=0.35, rely=0.60)
        
        ##Label CIDADE
        self.lb_city = Label(self.frame_top, text='CIDADE', bg='#C2D1F0', fg='#142952', font=('Bahnschrift SemiBold', 10, 'bold'))
        self.lb_city.place(relx=0.65, rely=0.60)
        
        
        
Frontend_configuaration_frame()