from tkinter import *
from config_back.config_db import Config_sqlite

class Create_functions_btn(Config_sqlite):
    def variaveis(self):
        self.code = self.ent_code.get()
        self.name = self.ent_name.get()
        self.phone = self.ent_phone.get()
        self.email = self.ent_email.get()
        self.city = self.ent_city.get()
        
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
        
        insert_db ='''
            INSERT INTO cliente(nome_cliente, email, telefone, cidade)
            VALUES( ?,?,?,?);
            '''
        print(f'Verificando se a função para cadastrar o cliente esta correta antes da execução:\n\n{insert_db}\nCliente cadastrado com sucesso\n')
        self.cursor.execute(insert_db, (self.name, self.email, self.phone, self.city))
        
        self.conn.commit()
        print('Cadastro realizada com sucesso\n')
        self.desconnect_db()
        
        self.select_client_list() # Atualiza a lista de clientes para mostrar os dados do novo cliente cadastrado
        self.clear_screen()
    
    def select_client_list(self):
        self.client_list.delete(*self.client_list.get_children())#Sempre que a função select foi utilizada, ela irá limpar a base
        
        self.connect_db()
        
        seleciona_cliente = '''
            SELECT id, nome_cliente, email, telefone, cidade FROM cliente 
                ORDER BY nome_cliente ASC;'''
        
        print(f'Verificando se a função para selecionar o cliente esta correta antes da execução:\n\n{seleciona_cliente}\n')        
        lista = self.cursor.execute(seleciona_cliente) #ORDER BY nome_cliente ASC responsável por chamar a lista em ordem alfabética
        
        for cliente in lista:
            self.client_list.insert('',  END, values=cliente)
        print('Seleção realizada com sucesso\n')
        
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
        
        deleta_cliente = '''DELETE FROM cliente WHERE id = ?'''
        print(f'Verificando se a função para deletar o cliente esta correta antes da execução:\n\n{deleta_cliente}\n')
        
        self.cursor.execute(deleta_cliente, (self.code))
        self.conn.commit()
        print('Exclusão realizada com sucesso\n')
        
        self.desconnect_db()
        self.clear_screen()
        self.select_client_list()
        
        
    def client_alter(self):
        self.variaveis()
        self.connect_db()
        
        alterar_cliente = ''' UPDATE cliente SET  nome_cliente=?, telefone=?, email=?, cidade=?
            WHERE id=?'''
        
        print(f'Verificando a conexão antes de realizar a alteração do cliente\n{alterar_cliente}\n')
        self.cursor.execute(alterar_cliente, (self.name, self.phone, self.email, self.city, self.code))
        self.conn.commit()
        print('Alteração realizada com sucesso\n')
        
        
        self.desconnect_db()
        self.select_client_list()
        self.clear_screen()