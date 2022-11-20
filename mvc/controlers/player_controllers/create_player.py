from mvc.models.player import Player
from cfg.dbconst import PLAYERS_TABLE

def create_player(player_instance: Player) -> None:
    '''
    We serialize the data and put it in the db. 
    We pop the ID because we don't need it to push data into db

    More info see create_tournament.py file in tournament model folder
    '''

    serialized_data = player_instance.__dict__
    serialized_data.pop('ID')

    PLAYERS_TABLE.insert(serialized_data)

    return None