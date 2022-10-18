from datetime import datetime
#porque necesito un tipo tiempo
import peewee

from app.v1.utils.db import db 
from .user_model import User
#es buena practica separar las importaciones 
class Todo(peewee.Model):
    
    title = peewee.CharField()
    create_at = peewee.DateTimeField(default = datetime.now)
    is_done = peewee.BooleanField(default=False)
    user = peewee.ForeignKeyField(User, backref="todos")
    
    class Meta:
        database = db