import os
import sys
import json

def greet(name):
    print(f"Hello, {name}")

def add(a, b):
    return a + b

class Config:
    DEBUG = True

    def __init__(self, options=[]):
        self.options = options

    def list(self):
        return self.options

flag = True
if flag == True:
    greet("world")
