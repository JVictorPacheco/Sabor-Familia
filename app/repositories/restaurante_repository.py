#imports: 
from app.models.restaurante import Restaurante
from app.utils.database_connection import DatabaseConnection

#class:
class RestauranteRepository:
    
#def's/funções
    def __init__(self, db_connection):
        self.db = db_connection 
            
            
    #CRUDS FUNÇOES
    def create_restaurant(self, restaurante: Restaurante) -> Restaurante:
        """
        Criar um novo restaurante no banco de dados
        """
        
        query = """INSERT INTO restaurantes 
                (nome, categoria) VALUES (%s, %s)
                RETURNING id, created_at, updated_at"""
    
        params = (restaurante.nome, restaurante.categoria)
        
        resultado = self.db.execute_query(query, params, fetch=True)
        
        #return resultado
        
        linha = resultado[0]
        return Restaurante(
            id=linha[0],
            categoria=restaurante.categoria,
            nome=restaurante.nome,
            created_at=linha[1],
            updated_at=linha[2]
        )


    def get_restaurant_by_id(self):
        pass



    def get_all_restaurant(self):
        pass



    def update_restaurant(self):
        pass


    def delete_restaurant(self):
        pass

          