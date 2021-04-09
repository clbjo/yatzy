from flask import Flask

app = Flask(__name__)

# not the same app as above, this one is this package
from app import routes

# Thanks to Miguel Grinberg and his Flask mega tutorial!

