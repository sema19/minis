'''
Created on Jun 29, 2019

@author: sedlmeier
'''
from flask import render_template


def start():
    return render_template('start.html')