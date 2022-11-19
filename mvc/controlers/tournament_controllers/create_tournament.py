from mvc.models.tournament import Tournament
from cfg.dbconst import TOURNAMENT_TABLE

def create_tournament(tournament_instance: Tournament) -> None :
    '''
    TinyDB uses a data entry format which is close to a python dictionary. The data which we need to serialize is, in fact
    the model/instance of the tournament. 
    To do that, we have a built-in python attribute which could help us here. 
    if we create a tournament, we suppose we don't have any dabatase ID entry. 

    TLDR; We use __dict__ python class attribute minus the 'ID' attribute to create a new Tournament in DB 
    '''
    serialized_data = tournament_instance.__dict__
    serialized_data.pop('ID')

    TOURNAMENT_TABLE.insert(serialized_data)

    # we could eventually return the previous line in order to get the ID of the db entry... 
    return None 
