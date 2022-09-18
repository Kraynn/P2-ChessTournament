import datetime


def get_tournament_title():
    tournament_title = input("Veuillez écrire le nom du tournoi :")
    return tournament_title


def get_tournament_location():
    tournament_location = input("Veuillez écrire la localisation du tournoi :")
    return tournament_location


def get_tournament_date():
    tournament_date = datetime.date.today()
    return tournament_date.strftime("%d/%m/%y")


def get_tournament_game_mode():
    tournament_gamemode = input("Veuillez saisir le mode de jeu du tournoi :")
    return tournament_gamemode


def get_tournament_description():
    tournament_description = input("Veuillez saisir la description relative au tournoi :")
    return tournament_description


def get_tournament_nb_of_rounds():
    tournament_nb_of_rounds = input("Veuillez saisir le nombre de rounds du tournoi :")
    return tournament_nb_of_rounds
