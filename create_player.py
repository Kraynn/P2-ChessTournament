from tinydb import TinyDB, Query
import views.v_add_player as vp
from models.player import Player


def register_player():
    print("Enregister un nouveau joueur: \n")
    name = vp.get_player_name()
    firstname = vp.get_player_firstname()
    birthdate = vp.get_player_birthdate()
    gender = vp.get_player_gender()
    ranking = vp.get_player_elo()
    data = {"Nom": name,
            "Prenom": firstname,
            "Date de naissance": birthdate,
            "Genre": gender,
            "Classement": ranking
            }
    player = Player(data)
    serialized_player = player.serialize()

    db = TinyDB("db.json")
    players_table = db.table("Joueurs")
    players_table.insert(serialized_player)

    reponse = input("Voulez-vous enregistrer un nouveau joueur? (O/N) : ")
    if reponse == "O":
        register_player()
    elif reponse == "o":
        register_player()
    else:
        pass


def show_players_rank():
    db = TinyDB("db.json")
    players_table = db.table("Joueurs")
    message = ''
    players = players_table.all()
    players.sort(key=lambda k: k['Classement'])
    print("Liste des joueurs et de leur classement: \n")
    for player in players:
        message += f'{player["Classement"]} {player["Nom"]} {player["Prenom"]} \n'
    print(message)


def update_ranking():
    db = TinyDB("db.json")
    User = Query()
    players_table = db.table("Joueurs")
    show_players_rank()
    player = input(" > Saissisez le nom de famille d'un joueur \n")
    new_rank = int(input(f"Quel est le nouveau classement de {player} ? \n"))
    players_table.upsert({"Classement": new_rank}, User.Nom == f"{player}")
    choice = input("> Voulez-vous modifier le classement d'un autre joueur? (O/N) \n")
    if choice == "O":
        update_ranking()
    elif choice == "o":
        update_ranking()
    else:
        pass
