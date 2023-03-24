from dotenv import load_dotenv
import os

load_dotenv()
database = os.getenv('DATABASE')
dbuser = os.getenv('DBUSER')
dbpassword = os.getenv('DBPASSWORD')