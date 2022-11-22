from mvc.models.tournament import Tournament
from mvc.models.round import Round

def generate_round(tournament: Tournament, name: str) -> None:
    current_round = Round(name=name)
    
    # Order by elo

    # match the pairs
