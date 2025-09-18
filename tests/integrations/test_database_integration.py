from app.config.database import get_db_connection



def test_integration():
        """
        CRIANDO TESTE DE CONEXAO/INTEGRACAO AO BANCO DE DADOS
        """
        
        #CRIAR CONEXAO
        db_conexao = get_db_connection()
        
        #VERIFICAR SE CONECTOU (USANDO ASSERT)
        assert db_conexao.connection is not None
        assert db_conexao.cursor is not None
        
        #FECHANDO CONEXAO
        db_conexao.close()
    
    
def test_connection_with_context_manager():
        """
        Testa se o context manager (with) 
        abre e fecha a conexão automaticamente.
        """
        with get_db_connection() as db_conexao:
            
            assert db_conexao.connection is not None
            assert db_conexao.cursor is not None
            
            
            
def test_execute_simple_query():
    """
    esta se consegue executar uma 
    query SQL simples.
    """
    
    with get_db_connection() as db_conexao:
        
       resultado = db_conexao.execute_query("SELECT 1", fetch=True)
       
       assert resultado is not None
       assert len(resultado) > 0
       assert resultado[0][0] == 1
       
       
            
            
            
        
        
