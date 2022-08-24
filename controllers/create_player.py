from tinydb import TinyDB
import views.v_add_player as vp
from models.player import Player

def register_player():

    print("Enregister un nouveau joueur: \n")
    name = vp.get_player_name()
    firstname = vp.get_player_firstname()
    birthdate = vp.get_player_birthdate()
    gender = vp.get_player_gender()
    ranking = vp.get_player_elo()
    data = {"Nom":name, "Prenom":firstname, "Date de naissance":birthdate, "Genre": gender, "Classement":ranking}
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