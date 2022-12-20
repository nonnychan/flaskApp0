from flask import Flask
 
app = Flask(__name__, static_folder='static')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] ='c10acc905bddc947adbb2c8999671d54763eb58b42d6dce4'
from app import views  # noqa
