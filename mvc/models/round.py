from dataclasses import dataclass
from datetime import datetime

@dataclass
class Round(object):

    name: str = None
    start: datetime = datetime.now()
    end: datetime = None
    matches: list = None #list of tuples see specs


