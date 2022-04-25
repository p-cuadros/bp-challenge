from flask import Flask
from Crypto.PublicKey import RSA
import os

private_key = RSA.generate(1024)
app = Flask( __name__ )

app.config['API_KEY'] = os.getenv('API_KEY')
app.config['PRIVATE_KEY'] =  private_key.export_key()
app.config['PUBLIC_KEY'] = private_key.publickey().export_key()

