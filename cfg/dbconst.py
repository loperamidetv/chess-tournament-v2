'''
This file aims to put all databases constants together. 
This includes table, database, paths, ...

'''

from tinydb import TinyDB

DATABASE_PATH = 'database.json'
TOURNAMENTS_TABLE = TinyDB(DATABASE_PATH).table('tournaments')
PLAYERS_TABLE = TinyDB(DATABASE_PATH).table('players')
