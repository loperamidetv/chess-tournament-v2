from dataclasses import dataclass
from datetime import date

@dataclass 
class Tournament: 
    '''
    Notice

    '''

    name: str
    location: str
    date_start: date
    date_end: date
    nb_rounds: int
    rounds: list
    players: list
    time_mode: str
    description: str 

    # create the basic crud operations