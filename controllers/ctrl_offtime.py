'''
Created on Jun 20, 2019

@author: sedlmeier
'''

from functools import partial
from connexion_sql_utils import crud
from models.offtime import Offtime

crudObj=Offtime

# crud functions Command
get     = partial(crud.get,     crudObj, limit=None, name=None)
post    = partial(crud.post,    crudObj, offtime_data=None)
get_id  = partial(crud.get_id,  crudObj, offtime_id=None)
put     = partial(crud.put,     crudObj, offtime_id=None, offtime_data=None)
delete  = partial(crud.delete,  crudObj, offtime_id=None)