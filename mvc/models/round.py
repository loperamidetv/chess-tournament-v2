from dataclasses import dataclass
from datetime import datetime

@dataclass
class Round(object):

    name: str = None
    start: datetime = None
    end: datetime = None
    matches: list = None #list of tuples see specs


