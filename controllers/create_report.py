from unittest.util import sorted_list_difference
from tinydb import TinyDB, Query
from pprint import pprint
from models.player import Player

def players_list(sorted_players):
    db = TinyDB("db.json")
    print('Liste de tous les acteurs par ordre alphabétique : \n')
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

