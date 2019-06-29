'''
Created on Jun 16, 2019

@author: sedlmeier
'''
from models.dbmodel import DbModel
from sqlalchemy import Column,String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime


class Offtime(DbModel):
    __tablename__ = 'offtimes'
    id          =   Column(String(100), primary_key=True)
    person_id   =   Column(String(100), ForeignKey("persons.id"))
    fade_in     =   Column(DateTime())
    start       =   Column(DateTime())
    end         =   Column(DateTime())
    fade_out    =   Column(DateTime())
        
    def __init__(self, person_id=None, fade_in=None, start=None, end=None, fade_out=None):
        self.person_id      =   person_id    
                
        self.fade_in   =   datetime.strptime(fade_in,"%Y-%m-%dT%H:%M:%SZ")
        self.start   =   datetime.strptime(start,"%Y-%m-%dT%H:%M:%SZ")
        self.end   =   datetime.strptime(end,"%Y-%m-%dT%H:%M:%SZ")
        self.fade_out   =   datetime.strptime(fade_out,"%Y-%m-%dT%H:%M:%SZ")