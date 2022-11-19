from dataclasses import dataclass

@dataclass
class Tournament(object):

    name: str
    location: str
    ID: int = None
    # W.I.P