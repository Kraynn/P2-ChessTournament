from pprint import pprint
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from models.player import Player
from views.main_menu import Menus
import controllers.create_player as cp
import controllers.create_round as cr
import controllers.create_tournament as ct
import controllers.create_report as crp
import views.v_add_player as vp 
import views.v_round as vr
import views.v_tournament as vt


#Voir variable nombre de rounds + ajuster le numero du round automatiquement
#Afficher joueurs des matchs avant de lancer les rounds + mettre à la fin le enditme + rendre heure de debut et de fin automatique
#factoriser fonctions sorting + finir de créer les rapports
#Créer variables explicit au lieu des chiffres magiques
#Fix inserting rounds data in create_round



def display_main_menu():
    pprint(Menus.main_menu)
    action = int(input("\n"))
    if action == 1: 
        display_player_menu()
    if action == 2: 
        display_tournament_menu()
    else:
        exit()

def display_player_menu():
    pprint(Menus.player_menu)
    action = int(input("\n"))
    if action == 1: 
        cp.register_player()
        print("Joueur(s) ajouté(s)")
        input("Appuyer sur une touche pour revenir en arrière")
        display_player_menu()
    if action == 2: 
        print("Afficher les rapports de joueurs") 
        display_players_report_menu()
        input("Appuyer sur une touche pour revenir en arrière")
        display_player_menu()            
    if action == 3: 
        display_main_menu()
    else:
        exit()

def display_tournament_menu():
    pprint(Menus.tournament_menu)
    action = int(input(""))
    if action == 1:
        ct.add_tournament()
        display_tournament_menu()
    if action == 2: 
        ct.show_tourneys()
        tournoi = input("Saisir le nom du tournoi \n")
        print("Début du tournoi \n")
        rounds = int(input("Combien de rounds voulez-vous jouer? \n "))
        for round in range(rounds):
            cr.start_round(tournoi)
        display_tournament_menu()
    if action == 3: 
        ct.show_tourneys()
        tournoi = input("Choisir un tournoi \n")
        rounds = int(input("Combien de rounds voulez-vous jouer? \n "))
        for round in range (rounds):
            cr.start_round(tournoi)
        display_tournament_menu()
    if action == 4: 
        print("Afficher les rapports de tournoi")
        display_tournaments_report_menu()                    #Creer des rapports
    if action == 5:
        display_main_menu()
        
def display_players_report_menu():
    pprint(Menus.players_report_menu)
    action = int(input("\n"))
    if action == 1:
        crp.sorted_players_names()
        input("Appuyer sur une touche pour revenir en arrière")
        display_players_report_menu()
    if action == 2: 
        crp.sorted_players_rankings()
        input("Appuyer sur une touche pour revenir en arrière")
        display_players_report_menu()
    if action == 3:
        display_main_menu()

def display_tournaments_report_menu():
    pprint(Menus.tournaments_report_menu)
    action = int(input("\n"))
    if action == 1:
        crp.show_all_tourneys()
        input("Appuyer sur une touche pour revenir en arrière")
        display_tournaments_report_menu()
    if action == 2:
        display_tournaments_report_menu_2()
    if action == 3:
        display_main_menu()
        

def display_tournaments_report_menu_2():
    ct.show_tourneys()
    tournoi = input("Veuillez saisir le nom d'un tournoi")
    pprint(Menus.tournaments_report_menu_2)
    action = int(input("\n"))
    if action == 1:
        pprint(Menus.players_report_menu)
        action_1 = int(input("\n"))
        if action_1 ==1:
            print(f"Classement des joueurs par odre alphabétique dans {tournoi} ")
            #fonction 
            input("Appuyer sur une touche pour revenir en arrière \n")
            display_tournaments_report_menu()
        if action_1 == 2:  
            print(f"Classement des joueurs par classement dans {tournoi} ")
            #fonction 
            input("Appuyer sur une touche pour revenir en arrière \n")
            display_tournaments_report_menu()  
        if action_1 ==3:
            display_tournaments_report_menu()
    if action == 2:
        print("Afficher les tours")
        #fonction
        input("Appuyer sur une touche pour revenir en arrière \n")
        display_tournaments_report_menu()  
    if action == 3:
        print("Afficher les matchs")
        #fonction
        input("Appuyer sur une touche pour revenir en arrière \n")
        display_tournaments_report_menu() 
    if action == 4: 
        display_tournament_menu()
    if action == 5: 
        display_main_menu()


pprint(Menus.main_menu_header)
print("\n")
display_main_menu()


