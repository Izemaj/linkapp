from flask import Flask

app = Flask(__name__,instance_relative_config=True)

app.config.from_pyfile("config.py")

from link_pkg.routes import routes

# from applawlist import mymodels


