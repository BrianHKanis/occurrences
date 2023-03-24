from settings import database, dbuser, dbpassword
from api import *

app = create_app(database, dbuser, dbpassword)
app.run(debug=True)