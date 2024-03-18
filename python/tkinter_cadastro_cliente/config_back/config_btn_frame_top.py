from tkinter import *
from config_back.config_db import Config_sqlite

class Create_functions_btn(Config_sqlite):
    
    def variaveis(self):
        self.code = self.ent_code.get()
        self.name = self.ent_name.get()
        self.phone = self.ent_phone.get()
        self.email = self.ent_email.get()
        self.city = self.ent_city.get()
        
    def functions(self):
        self.desconnect_db()
        self.clear_screen()
        self.select_client_list()
        
    def clear_screen(self):
        self.ent_code.delete(0, END)
        self.ent_name.delete(0, END)
        self.ent_phone.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_city.delete(0, END)
    
    def add_client(self):
        '''Função responsável por inserir cliente na tabela'''
        self.variaveis()
        
        self.connect_db()
        
        self.insert_data()

        self.desconnect_db()

        self.select_client_list() # Atualiza a lista de clientes para mostrar os dados do novo cliente cadastrado

    def select_client_list(self):
        self.client_list.delete(*self.client_list.get_children())#Sempre que a função select foi utilizada, ela irá limpar a base
        self.connect_db()   
        self.select_data()
        self.desconnect_db()
    
    def on_double_click(self,event):
        self.clear_screen()
        self.client_list.selection()
        
        for cliente in self.client_list.selection():
            col1,col2,col3,col4,col5 = self.client_list.item(cliente, 'values')
            self.ent_code.insert(END, col1)
            self.ent_name.insert(END, col2)
            self.ent_email.insert(END, col3)
            self.ent_phone.insert(END, col4)
            self.ent_city.insert(END, col5)
    
    def client_delete(self):
        print('\nIniciando o processo de exclusão do cliente\n')
        self.variaveis()
        self.connect_db()
        self.delete_data()
        self.functions()
    
    def client_alter(self):
        print('\nIniciando o processo de atualização de cadastro\n')
        self.variaveis()
        self.connect_db()
        self.alter_data()
        self.functions()
        
    def client_search(self):
        self.connect_db()
        
        self.client_list.delete(*self.client_list.get_children())
        self.ent_name.insert(END, '%') # usada para adicionar um caractere especial (%) no final do conteúdo do widget self.ent_name para facilitar a busca de dados no banco de dados, uma vez que o caractere % é frequentemente usado como um caractere curinga em consultas SQL para representar um conjunto de caracteres desconhecidos.
        
        self.search_data()
        
        self.clear_screen()
        
        self.desconnect_db()
        
        