# -*- coding: utf-8 -*-

from dataclasses import dataclass
from utils.custom_datetime import CustomDate
from faker import Faker
from random import randrange
from cfg.dbconst import PLAYERS_TABLE

@dataclass
class Player(object):

    ID: int = None
    first_name: str = None
    last_name: str = None
    birthdate: CustomDate = None 
    gender: str = None
    elo: int = None

    '''
    Basic CRUD operations
    
    '''


    def create(self) -> None:
        serialized_data = self.__dict__
        serialized_data.pop('ID')
        serialized_data['birthdate'] = (f"{serialized_data['birthdate'].day}/{serialized_data['birthdate'].month}/{serialized_data['birthdate'].year}")
        PLAYERS_TABLE.insert(serialized_data) 
    
    def read(self) -> None:
        serialized_data = PLAYERS_TABLE.get(doc_id=self.ID)

        for key, value in serialized_data.items():
            if (key != 'ID'):
                self.__dict__[key] = value


    '''
    Advanced features
    
    '''

    def random(self) -> None:
        '''
        Generate fake identity and push it onto object attributes

        '''
        #We need to generate fake data and filter name, birthdate and gender
        random_data = Faker('fr_FR').profile()
        random_data = {key:value for (key, value) in random_data.items()
                        if (key == 'name') or (key == 'birthdate') or (key == 'sex')}

        # Faker lib doesn't separate the first and the last name, 
        # which we do here
        name = random_data['name'].split()
        random_data.pop('name')

        # just some basic cleaning...
        random_data['first_name'], random_data['last_name'] = name[0], name[1]

        del name

        # Push onto attributes
        self.first_name = random_data['first_name']
        self.last_name = random_data['last_name']
        self.birthdate = random_data['birthdate']
        self.gender = random_data['sex']
        self.elo = randrange(start= 1250, stop= 2500) # we keep it simple here, but doesn't have any statistical acuracy...



