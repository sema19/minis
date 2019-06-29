'''
Created on May 11, 2019

@author: sedlmeier
'''

from models.dbmodel import DbModel
from sqlalchemy import Column,String

class Person(DbModel):
    __tablename__ = 'persons'
    id          =   Column(String(100), primary_key=True)
    firstname   =   Column(String(300))
    lastname    =   Column(String(300))
        
    def __init__(self, firstname, lastname):
        self.firstname      =   firstname        
        self.lastname   =   lastname
       
             
    