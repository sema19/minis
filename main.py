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

logging.basicConfig(level=logging.DEBUG)

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)
flask_app = connex_app.app
#flask_app.templates_folder="web/templates"
login_manager = LoginManager(flask_app)
Bootstrap(flask_app)

connex_app.add_api('api/minis.yaml')


if __name__ == '__main__':
    
    # run our standalone gevent server
    dbmodel.Create()
    connex_app.run(host='0.0.0.0', port=80, threaded=True, debug=True)        # 0.0.0.0 allows all eth interfaces to access (localhost, 10.*.*.*)
    
