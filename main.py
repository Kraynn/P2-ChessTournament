from pprint import pprint
from views.main_menu import Menus
import controllers.create_player as cp
import controllers.create_round as cr
import controllers.create_tournament as ct
import controllers.create_report as crp


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
        input("> Appuyer sur une touche pour revenir en arrière")
        display_player_menu()
    if action == 2:
        print("Afficher les rapports de joueurs")
        display_players_report_menu()
        input("> Appuyer sur une touche pour revenir en arrière")
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
        tournoi = input("> Saisir le nom du tournoi \n")
        print("Début du tournoi \n")
        cr.round_check(tournoi)
        display_tournament_menu()
    if action == 3:
        ct.show_tourneys()
        tournoi = input("> Choisir un tournoi \n")
        cr.round_check(tournoi)
        display_tournament_menu()
    if action == 4:
        print("Afficher les rapports de tournoi")
        display_tournaments_report_menu()
    if action == 5:
        display_main_menu()


def display_players_report_menu():
    pprint(Menus.players_report_menu)
    action = int(input("\n"))
    if action == 1:
        print('Liste de tous les joueurs par ordre alphabétique : \n')
        crp.sorted_players_names()
        input("> Appuyer sur une touche pour revenir en arrière")
        display_players_report_menu()
    if action == 2:
        print('Liste de tous les acteurs par classement: \n')
        crp.sorted_players_rankings()
        input("> Appuyer sur une touche pour revenir en arrière")
        display_players_report_menu()
    if action == 3:
        display_main_menu()


def display_tournaments_report_menu():
    pprint(Menus.tournaments_report_menu)
    action = int(input("\n"))
    if action == 1:
        crp.show_all_tourneys()
        input("> Appuyer sur une touche pour revenir en arrière")
        display_tournaments_report_menu()
    if action == 2:
        display_tournaments_report_menu_2()
    if action == 3:
        display_main_menu()


def display_tournaments_report_menu_2():
    ct.show_tourneys()
    tournoi = input("> Veuillez saisir le nom d'un tournoi \n")
    pprint(Menus.tournaments_report_menu_2)
    action = int(input("\n"))
    if action == 1:
        pprint(Menus.players_report_menu)
        choice = int(input("\n"))
        if choice == 1:
            print(f"Classement des joueurs par odre alphabétique dans {tournoi}\n")
            crp.players_in_tn_by_names(tournoi)
            input("> Appuyer sur une touche pour revenir en arrière \n")
            display_tournaments_report_menu()
        if choice == 2:
            print(f"Classement des joueurs par classement dans {tournoi} ")
            crp.players_in_tn_by_rankings(tournoi)
            input(" > Appuyer sur une touche pour revenir en arrière \n")
            display_tournaments_report_menu()
        if choice == 3:
            display_tournaments_report_menu()
    if action == 2:
        print("Afficher les Manches")
        crp.show_all_rounds(tournoi)
        input("> Appuyer sur une touche pour revenir en arrière \n")
        display_tournaments_report_menu()
    if action == 3:
        print("Afficher les matchs")
        crp.show_all_matchs(tournoi)
        input("> Appuyer sur une touche pour revenir en arrière \n")
        display_tournaments_report_menu()
    if action == 4:
        display_tournament_menu()
    if action == 5:
        display_main_menu()


pprint(Menus.main_menu_header)
print("\n")
display_main_menu()
