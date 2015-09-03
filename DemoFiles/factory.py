__author__ = 'StefanFlorescu'

import json

class JSONConnector:
    def __init__(self, filepath = "C:/UsersStefanFlorescu/Desktop/JSON sources/self-employed.json"):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data



class Test():

    def __init__(self):
        self.name = "Test 1"
        self.surename = "Surename"

def Obj_func(instance = None):

    print instance.name
    print instance.surename


    