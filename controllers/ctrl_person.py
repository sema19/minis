'''
Created on Jun 20, 2019

@author: sedlmeier
'''

from functools import partial
from connexion_sql_utils import crud
from models.person import Person

def add_api(connex_app):
    connex_app.add_api('controller/person.yaml')

crudObj=Person

# crud functions Command
get     = partial(crud.get,     crudObj, limit=None, name=None)
post    = partial(crud.post,    crudObj, person_data=None)
get_id  = partial(crud.get_id,  crudObj, person_id=None)
put     = partial(crud.put,     crudObj, person_id=None, person_data=None)
delete  = partial(crud.delete,  crudObj, person_id=None)