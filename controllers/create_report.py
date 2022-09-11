from tinydb import TinyDB, Query
from models.player import Player
from pprint import pprint

def players_list(sorted_players):
    db = TinyDB("db.json")
    for player in sorted_players:
            print(f"NOM: {player['Nom']} \n"
                  f" PRENOM: {player['Prenom']} \n"
                  f" DATE DE NAISSANCE: {player['Date de naissance']} \n"
                  f" GENRE: {player['Genre']} \n"
                  f" CLASSEMENT: {player['Classement']} \n")

def sorted_players_names():                                                     #Refactoriser pour raccourcir le code
    db = TinyDB("db.json")
    players_table = db.table("Joueurs")
    sorted_players = sorted(players_table, key=lambda k: k['Nom'])
    players_list(sorted_players)

def sorted_players_rankings():
    db = TinyDB("db.json")
    players_table = db.table("Joueurs")
    sorted_players = sorted(players_table, key=lambda k: k['Classement'])
    players_list(sorted_players)

def show_all_tourneys():
    db = TinyDB("db.json")
    tn_table = db.table("Tournois")
    for tournament in tn_table:
        print(f"NOM DU TOURNOI : {tournament['Titre']:} \n"
              f"LIEU : {tournament['Lieu']} \n"
              f"DATE : {tournament['Date']} \n"
              f"MODE DE JEU : {tournament['Mode de jeu']} \n"
              f"DESCRIPTION : {tournament['Description']} \n"
              f"NOMBRES DE MANCHES : {tournament['Nombre de manches']} \n")

def players_in_tn_by_rankings(tournoi):
    db = TinyDB('db.json')
    players_table = db.table("Joueurs")
    tn_table = db.table("Tournois")
    User = Query()
    tournoi = tournoi
    i = len(tn_table.get(User.Titre == f"{tournoi}")["Joueurs"])
    for player in players_table:
        x = tn_table.search(User.Titre == f"{tournoi}")[0]              
        y = x["Joueurs"]
    players = [x for x in players_table if x.doc_id in y]
    playerModels = [Player(x) for x in players]
    playerModels.sort(key=lambda k: k.elo)
    for i in range(i):  
        print(f"NOM : {playerModels[i].name} \n"
              f"PRENOM : {playerModels[i].first_name} \n"
              f"DATE DE NAISSANCE : {playerModels[i].birthdate} \n"
              f"GENRE : {playerModels[i].gender} \n"
              f"CLASSEMENT : {playerModels[i].elo} \n")

def players_in_tn_by_names(tournoi):
    db = TinyDB('db.json')
    players_table = db.table("Joueurs")
    tn_table = db.table("Tournois")
    User = Query()
    tournoi = tournoi
    i = len(tn_table.get(User.Titre == f"{tournoi}")["Joueurs"])
    for player in players_table:
        x = tn_table.search(User.Titre == f"{tournoi}")[0]              
        y = x["Joueurs"]
    players = [x for x in players_table if x.doc_id in y]
    playerModels = [Player(x) for x in players]
    playerModels.sort(key=lambda k: k.name)
    for i in range(i):  
        print(f"NOM : {playerModels[i].name} \n"
              f"PRENOM : {playerModels[i].first_name} \n"
              f"DATE DE NAISSANCE : {playerModels[i].birthdate} \n"
              f"GENRE : {playerModels[i].gender} \n"
              f"CLASSEMENT : {playerModels[i].elo} \n")
    
def show_all_rounds(tournoi):
    db = TinyDB("db.json")
    tn_table = db.table("Tournois")
    User = Query()
    rounds = tn_table.get(User.Titre == f"{tournoi}")["Manches"]
    for round in rounds:
        print(round)