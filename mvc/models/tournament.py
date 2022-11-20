from dataclasses import dataclass
from datetime import datetime

@dataclass
class Tournament(object):

    name: str = None
    location: str = None
    date_start: datetime = None
    date_end: datetime = None
    number_of_rounds: int = None
    rounds: list = None
    players: list = None
    time_mode: str = None
    rounds: list = None # list of Round instances
    description: str = None
    ID: int = None