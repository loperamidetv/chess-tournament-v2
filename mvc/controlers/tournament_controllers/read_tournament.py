from mvc.models.tournament import Tournament
from cfg.dbconst import TOURNAMENTS_TABLE

def read_tournament(ID: int, tournament_instance: Tournament) -> None:
    '''
    Given the ID, the function aims to gather the data from the database 
    and update the tournament instance attributes with the data
    '''
    tournament_db_data = TOURNAMENTS_TABLE.get(doc_id=ID)

    # Updating the object Tournament attributes
    for key, value in tournament_db_data.items():
        tournament_instance.__dict__[key] = value

    # Updating the ID, because the ID doesn't appear in 
    # the tournament data from DB
    tournament_instance.ID = ID

    return None