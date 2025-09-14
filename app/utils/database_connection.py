import sys
import os


# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import psycopg2


class DatabaseConnection:
    
    def __init__(self, dbname, user, password, host, port ):
        """
        Inicializa os parâmetros de conexão
        """
        self.connection_parameters = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        }
        
        self.connection = None
        self.cursor     = None
        
        
        
    def connect(self):
        """
        Estabelece a conexão com o banco de dados.
        """
        try:
            self.connection = psycopg2.connect(**self.connection_parameters)
            self.cursor     = self.connection.cursor()
            print('Conexão bem Sucedida')
        except Exception as e:
            print(f'Erro ao conectar no banco de dados {e}')
            raise
        
        
    def execute_query(self, query, params=None, fetch=False):
        """
        Realiza um/uma script/query quando esta conectado ao banco de dados
        """
        try:
            if not self.cursor:
                raise RuntimeError('Cursor não disponivel. Conecte-se primeiro')
            
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall() if fetch else None
            
            
            
        except Exception as e:
            print(f'Erro ao executar a query {e}')
            self.rollback()
            return None
        
        
        
    def commit(self):
        """
        Confirmar alterações no banco de dados
        """
        
        if self.connection:
            self.connection.commit()
            
            
            
    def close(self):
        """
        Fecha a conexão com o banco de dados
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            
            
            
            
    def rollback(self):
        """
        Reverte as alterações não confirmadas no banco de dados.
        """
        if self.connection:
            self.connection.rollback()
            print('Rollback Realizado')
            
            
            
    def __enter__(self):
        self.connect()
        return self
    
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.rollback()
        self.close()
        
            
        
        