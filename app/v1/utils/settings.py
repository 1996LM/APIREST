import os 
#os : operation sistem es una herramienta muy util para trabajar con las variables de entorno

from pydantic import BaseSettings
#pydantic es util porque obliga a tipar
#lo que distingue a fastapi de las demas es que es mas rapida
from dotenv import load_dotenv
load_dotenv()

class settings(BaseSettings):
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')


    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')