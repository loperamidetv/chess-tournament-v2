from tinydb import TinyDB
from abc import ABC

class DBHandler(ABC):

    def __init__(self, TABLE: TinyDB):
        self.TABLE = TABLE

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

