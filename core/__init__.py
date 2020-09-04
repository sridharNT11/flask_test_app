from flask import Flask 
app = Flask(__name__)


app.config.from_object('core.config.SECRET_KEY')
app.config.from_object('core.config.Config')


config = app.config



#from core import routes
from core.controller.custcontroller import app as cust

app.register_blueprint(cust, url_prefix='')