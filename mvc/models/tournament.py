from dataclasses import dataclass
from datetime import date

@dataclass
class Tournament(object):

    name: str = None
    location: str = None
    date_start: date = None
    date_end: date = None
    number_of_rounds: int = None
    rounds: list = None
    players: list = None
    time_mode: str = None
    description: str = None
    ID: int = None