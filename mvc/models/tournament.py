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
    date_start: datetime = datetime.now()
    date_end: datetime = None
    number_of_rounds: int = 4
    time_mode: str = None
    description: str = None
    
    '''
    Complexe attributes

    '''

    # Warning: the tournament instance contains the intances of the objects below
    # but the db contains ID only!
    rounds: list = []
    players: list = []
    

    '''
    Basic CRUD operations

    '''

    def create(self) -> None:
        '''
        Pretty straighforward method

        And I'll regret writing that later... 

        '''
        serialized_data = self.__dict__
        serialized_data.pop('ID')

        self.ID = TOURNAMENTS_TABLE.insert(serialized_data)
        
        # we could eventually return the previous line in order to get the ID of the db entry... 
        return None

    def read(self) -> None:
        for key, value in TOURNAMENTS_TABLE.get(doc_id=self.ID).items():
            self.__dict__[key] = value
            

    def update(self) -> None:
        '''
        For an unknown reason, when initialize data = self.__dict__, this modifies
        the tournament itself, maybe it's because python itself, probably a memory pointer thing 
        related... Didn't dig a lot on this... I love you python, but you made me lost an hour on this...
        '''
        
        data = {}

        '''
        Basically, it gets all the attributes, thks to self.dict thing
        run through it and update the data. 
        I don't need an ID updating. (this'd be non sense...)
        so I ditch the ID part (by if-ing...)
        '''
        for key, value in self.__dict__.items():
            if (key != 'ID'):
                data[key] = value


        TOURNAMENTS_TABLE.update(data, doc_ids=[self.ID])

        return None



    def delete(self) -> None:
        pass


    '''
    OOP human-readable methods. 

    '''
    def add_players(self, *args):
        pass

    def rank_by_elo(self):
        pass

    def rank_by_score(self):
        pass