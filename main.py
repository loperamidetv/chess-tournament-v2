from mvc.controlers.tournament_controllers.read_tournament import read_tournament
from mvc.models.tournament import Tournament


def run() -> None:
    tournament = Tournament()

    read_tournament(2, tournament)

    print(tournament)
    

if (__name__ == "__main__"):
    run()