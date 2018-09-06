from pymongo import MongoClient


class Store:
    def __init__(self):
        self.conn = MongoClient('localhost', 27017)
        self.db = self.conn['isr']