from dataclasses import dataclass
from datetime import datetime
from cfg.dbconst import TOURNAMENTS_TABLE

@dataclass
class Tournament(object):

    '''
    Basic attributes

    '''
    ID: int = None
    name: str = None
    location: str = None
    date_start: datetime = None
    date_end: datetime = None
    number_of_rounds: int = 4
    time_mode: str = None
    description: str = None
    
    '''
    Complexe attributes

    '''
    rounds: list = None
    players: list = None
    

    '''
    Basic CRUD operations

    '''

    def create(self) -> None:
        serialized_data = self.__dict__
        serialized_data.pop('ID')

        TOURNAMENTS_TABLE.insert(serialized_data)

        # we could eventually return the previous line in order to get the ID of the db entry... 
        return None

    def read(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass


    '''
    OOP human-readable methods. 

    '''
    def add_players(self):
        pass

    def rank_by_elo(self):
        pass

    def rank_by_score(self):
        pass