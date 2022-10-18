from enum import unique
import peewee

from app.v1.utils.db import db 
#

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()
    
    class Meta:
        #para que sepa a que base de datos esta apuntando
        database = db 