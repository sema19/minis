'''
Created on Jun 20, 2019

@author: sedlmeier
'''
from models.dbmodel import DbModel
from sqlalchemy import Column,String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime


class Ministrant(DbModel):
    __tablename__ = 'ministranten'
    id          =   Column(String(100), primary_key=True)
    person_id   =   Column(String(100), ForeignKey("persons.id"))
    since       =   Column(DateTime())
    tel_home    =   Column(String(100))
    tel_mobile  =   Column(String(100))
    email       =   Column(String(300))
        
    def __init__(self, person_id=None, since=None, tel_home=None, tel_mobile=None, email=None):
        self.person_id      =   person_id    
        self.since   =   datetime.strptime(since,"%Y-%m-%dT%H:%M:%SZ")
        self.tel_home   =   tel_home
        self.tel_mobile   =   tel_mobile
        self.email   =   email