from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Restaurante(BaseModel):
    id: Optional[int] = None
    nome: str
    categoria: Optional[str] = None
    
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    
    
    
    
    
    