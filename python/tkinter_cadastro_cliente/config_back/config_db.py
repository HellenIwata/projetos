from tkinter import *
import sqlite3

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