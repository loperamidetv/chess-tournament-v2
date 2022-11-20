from dataclasses import dataclass
from datetime import date

@dataclass
class Player(object):

    first_name: str = None
    last_name: str = None
    do_birth: date = None 
    gender: str = None
    elo: int = None
    ID: int = None