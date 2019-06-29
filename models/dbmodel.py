'''
Created on May 11, 2019

@author: sedlmeier
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from connexion_sql_utils import BaseMixin

DB_URI='sqlite:///db/minis.sqlite3'

engine = create_engine(DB_URI)

from sqlalchemy import String

'''
class PKeyType: String();
    def __init__():
        super.String(100)
'''        

Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
    )
                         
class MyBase(BaseMixin):
    @staticmethod
    def session_maker():
        return Session()
    def __str__(self):
        return "%s"%(str(self.dump()))    
    def dump(self):
        return dict([(k,v) for k,v in vars(self).items() if not k.startswith('_')])


DbModel = declarative_base(cls=MyBase)

   
def Create():
    DbModel.metadata.create_all(bind=engine)
