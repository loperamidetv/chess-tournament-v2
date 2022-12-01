

from dataclasses import dataclass, field
from datetime import datetime
from faker import Faker
from cfg.dbconst import TOURNAMENTS_TABLE, PLAYERS_TABLE
from random import choice, randrange
from mvc.models.player import Player

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
    rounds: list[int] = field(default_factory=list)
    players: list[int] = field(default_factory=list)
    # ...                ^^^^^^^^^ WTF?
    

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
        serialized_players = [ID for ID in self.__dict__['ID']]
        serialized_data['ID'] = serialized_players
        
        self.ID = TOURNAMENTS_TABLE.insert(serialized_data)

        print(serialized_data)
        
        # we could eventually return the previous line in order to get the ID of the db entry... 
        return None

    def read(self) -> None:
        for key, value in TOURNAMENTS_TABLE.get(doc_id=self.ID).items():
            self.__dict__[key] = value

        player_instances_list = list()
        for player_ID in self.__dict__['players']:
            player = Player(ID=player_ID)
            player.read()
            player_instances_list.append(player)
        self.players = player_instances_list
        del player_instances_list
        
     

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

    def random(self):
        fake_data = Faker('fr_FR')
        self.name = fake_data.name()
        self.location = fake_data.city()
        self.time_mode = choice(['blitz', 'bullet', 'coup rapide'])

        # Select some random player in db
       


    def add_player_instances(self, *args: Player) -> None:
        for player in args:
            self.players.append(player)

        return None

    def serialize_players(self) -> None:
        self.players = [player.ID for player in self.players]       
        return None
    
    def rank_by_elo(self):
        pass

    def rank_by_score(self):
        pass