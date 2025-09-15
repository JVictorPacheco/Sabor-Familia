from app.config.database import get_db_connection



def test_integration():
    '''
    CRIANDO TESTE DE CONEXAO/INTEGRACAO AO BANCO DE DADOS
    '''
    
    #CRIAR CONEXAO
    db_conexao = get_db_connection()
    
    #VERIFICAR SE CONECTOU (USANDO ASSERT)
    assert db_conexao.connection is not None
    assert db_conexao.cursor is not None
    
    #FECHANDO CONEXAO
    db_conexao.close()
    
    