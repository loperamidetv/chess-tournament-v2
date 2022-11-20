from mvc.models.player import Player
from cfg.dbconst import PLAYERS_TABLE

def read_player(ID: int, player_instance: Player) -> None:
    '''
    Given the ID, the function aims to gather the data from the database 
    and update the player instance attributes with the data
    '''

    player_db_data = PLAYERS_TABLE.get(doc_id=ID)

    # Updating the Player instance's attributes
    for key, value in player_db_data.items():
        player_instance.__dict__[key] = value

    # Updating the ID, because the ID doesn't appear in 
    # the tournament data from DB
    player_instance.ID = ID


    return None

