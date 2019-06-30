'''
Created on May 11, 2019

@author: sedlmeier
'''

import os
import connexion
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import logging
from models import dbmodel
from controllers import ctrl_web

import configparser

settings = configparser.ConfigParser()
settings.read("minis.ini")   

logging.basicConfig(level=logging.DEBUG)

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)
flask_app = connex_app.app
#flask_app.templates_folder="web/templates"
#login_manager = LoginManager(flask_app)
Bootstrap(flask_app)
flask_app.config['BOOTSTRAP_SERVE_LOCAL'] = True
#flask_app.templates_folder="web"

connex_app.add_api('api/minis.yaml')
connex_app.add_url_rule('/','index',ctrl_web.start)



if __name__ == '__main__':
    
    # run our standalone gevent server
    dbmodel.Create()
    host=settings.get("webserver","host")   #'0.0.0.0'
    port=settings.get("webserver","port")   #'80'
    dbg=settings.getboolean("webserver","debug") 
    connex_app.run(host=host, port=port, threaded=True, debug=dbg)        # 0.0.0.0 allows all eth interfaces to access (localhost, 10.*.*.*)
    
