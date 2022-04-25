from flask import Flask
from Crypto.PublicKey import RSA
#from flask_wtf.csrf import CSRFProtect
import os

private_key = RSA.generate(2048)
app = Flask( __name__ )
# csrf = CSRFProtect()
# csrf.init_app(app)
# app.secret_key = os.getenv('API_KEY')
# app.config['SECRET_KEY'] = os.getenv('API_KEY')
app.config['API_KEY'] = os.getenv('API_KEY')
app.config['PRIVATE_KEY'] =  private_key.export_key()
app.config['PUBLIC_KEY'] = private_key.publickey().export_key()

