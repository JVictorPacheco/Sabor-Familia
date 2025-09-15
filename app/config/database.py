from app.utils.database_connection import DatabaseConnection


DB_CONFIG_CONNECT = {
      'dbname':   'biblego',
      'user':     'biblego',
      'password': 'biblego%123!',
      'host':     '177.70.98.148',
      'port':     '6543'
    
}



def get_db_connection():
    """
    Cria e retorna uma conexão ativa com o banco de dados PostgreSQL.
    
    Returns: DatabaseConnection: Instância conectada ao banco biblego
    """
    db_connection = DatabaseConnection(**DB_CONFIG_CONNECT)
    db_connection.connect()
    return db_connection
    