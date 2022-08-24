from tinydb import TinyDB, Query
import views.v_tournament as vt
from models.tournament import Tournament

def add_tournament():
    title = vt.get_tournament_title()
    location = vt.get_tournament_location()
    date = vt.get_tournament_date()
    game_mode = vt.get_tournament_game_mode()
    description = vt.get_tournament_description()
    nb_of_rounds = vt.get_tournament_nb_of_rounds()
    tournament = Tournament(title, location, date, game_mode, description, nb_of_rounds)
    serialized_tournament = tournament.serialize()
    
    db = TinyDB("db.json")
    tournaments_table = db.table("Tournois")
    tournaments_table.insert(serialized_tournament)
    add_player_to_tn(title)

    reponse = input("Voulez-vous enregistrer un nouveau tournoi? (O/N) : ")
    if reponse == "O": 
        add_tournament()
    if reponse == "o":
        add_tournament()
    else:
        pass
    return title

def show_players():
    db = TinyDB("db.json")
    players_table = db.table("Joueurs")
    message = ''
    players = players_table.all()
    for player in players:
        message += f'{player.doc_id} {player["Nom"]} {player["Prenom"]} \n'
    print(message)

def add_player_to_tn(tournoi):
    db = TinyDB("db.json")
    User = Query()
    tn_table = db.table("Tournois")
    players = []
    print("Ajouter de sjoueurs au tournoi")
    show_players()
    for i in range(8):
        player = int(input("Choisir un id de joueur"))
        players.append(player)
    tn_table.update({"Joueurs": players}, User.Titre==f"{tournoi}")

def show_tourneys():
    db = TinyDB("db.json")
    tn_table = db.table("Tournois")
    message = ''
    tournaments = tn_table.all()
    for tournament in tournaments:
        message += f'-- {tournament["Titre"]} \n'
    print(message)
