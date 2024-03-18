from tkinter import *
import sqlite3
import os
from tkinter.messagebox import showerror

class Config_sqlite():
    def connect_db(self):
        '''Função responsável por conectar na base de dados "clientes.db" '''
        
        print('Por favor, aguarde... Conectando ao banco de dados \n') 
        self.conn  = sqlite3.connect('clientes.db') #Criando o conector do banco
        self.cursor = self.conn.cursor() 
        
    # função responsável por desconectar o banco de dados
    def desconnect_db(self):
        '''Função responsável por desconectar do banco de dados'''
        print('Por favor, aguarde... Desconectando do banco de dados \n') 
        self.conn.close() #  Fechamento da conexão com o Banco de Dados
    
    #Criar tabela de clientes
    def create_tb_client(self):
        '''Função responsável por criar a tabela cliente dentro da base clientes'''
        self.connect_db()
    
        #Criando a tabela
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cliente VARCHAR(100) NOT NULL,
                email  VARCHAR(100) UNIQUE NOT NULL,
                telefone INTEGER(15),
                cidade VARCHAR(2)
            )
        ''')
        self.conn.commit()
        
        print('Banco de dados criado\n')
        
        self.desconnect_db()
        
        os.system('cls')
    
    def insert_data(self):
        os.system('cls')
        insert_data = '''INSERT INTO cliente(nome_cliente, email, telefone, cidade)
            VALUES( ?,?,?,?);'''
        
        print(f'Validando o script de insert antes da execução\n{insert_data}\n')
        
        self.cursor.execute(insert_data,(self.name, self.email, self.phone, self.city))
        self.conn.commit()
        print('\nCadastro relizado com sucesso\n')
    
    def select_data(self):
        os.system('cls')
        #ORDER BY nome_cliente ASC responsável por chamar a lista em ordem alfabética
        select_data = '''SELECT id, nome_cliente, email, telefone, cidade FROM cliente 
            ORDER BY nome_cliente ASC;'''
        
        print(f'Validando o script de seleção antes da execução\n{select_data}\n')
        
        tb_client = self.cursor.execute(select_data)
        
        for cliente in tb_client:
            self.client_list.insert('',  END, values=cliente)
        print('Seleção realizada com sucesso\n')
    
    def alter_data(self):
        os.system('cls')
        update_data = '''UPDATE cliente SET nome_cliente= ?, telefone=?, email=?, cidade=?
            WHERE id=?'''
        
        print(f'Validando o script de atualização antes da execução\n{update_data}\n')
        self.cursor.execute(update_data, (self.name, self.phone, self.email, self.city, self.code))
        self.conn.commit()
        
        print('Alteração realizada com sucesso\n')        

    def delete_data(self):
        os.system('cls')
        delete_data = '''DELETE FROM cliente 
            WHERE id = ?'''
        print(f'Validando o script de exclusão antes da execução\n{delete_data}\n')
    
        self.cursor.execute(delete_data, (self.code))
        self.conn.commit()
    
        print('Exclusão realizada com sucesso\n')

    def search_data(self):
        os.system('cls')
        name = self.ent_name.get()
        
        if name:
            search_data = ('''
            SELECT id, nome_cliente, email, telefone, cidade FROM cliente
            WHERE nome_cliente
            LIKE "%s"
            ORDER BY nome_cliente ASC'''
            % name)
        
        print(f'Validando o script de busca antes da execução\n{search_data}\n')
        
        self.cursor.execute(search_data)
        search = self.cursor.fetchall() # .fetchall() = Função utilizada para retornar uma lista de tuplas, onde cada tupla representa uma linha da tabela do banco de dados. Neste caso, ele obtém todos os resultados da consulta SQL executada anteriormente.
        for cliente in search:
            self.client_list.insert('', END, values=cliente)
        else:
            showerror("Erro", "Nenhum resultado encontrado")
    
    