from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from SLCTFRM import csi3335fall2021 as cfg
import pymysql


app = Flask(__name__)
app.config['SECRET_KEY'] = '939a1ee77bf825cf3fb65f05e9b8358c'  # key for password encryption
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}:3306/{3}".format(cfg.mysql['username'], cfg.mysql['password'],
                                                                                      cfg.mysql['host'], cfg.mysql['database'])
con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['username'], password=cfg.mysql['password'], database=cfg.mysql['database'])
cur = con.cursor()
login_manager = LoginManager(app)
login_manager.login_view = 'loginpage'
login_manager.login_message_category = 'info'
_bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
db.create_all()

from SLCTFRM import routes
