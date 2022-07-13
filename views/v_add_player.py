from models.player import Player

# def add_player_info():
#     """
#     Demande les informations relatives à un joueur et les enregistre
#     """   
#     name = input("Veuillez écrire le nom de famille du joueur")
#     first_name = input("Veuillez écrire le prénom de famille du joueur")
#     birthdate = input("Veuillez saisir la date de naissance du joueur (JJMMAAAA)")
#     gender = input("Veuillez saisir le genre du joueur (M ou F)") 
#     elo = input("Veuillez saisir le classement du joueur")
#     return (name, first_name, birthdate, gender, elo)

def get_player_name():
    player_name = input("Veuillez écrire le nom de famille du joueur: ")
    return player_name

def get_player_firstname():
    player_surname = input("Veuillez écrire le prénom de famille du joueur : ")
    return player_surname

def get_player_birthdate():
    player_birthdate = input("Veuillez saisir la date de naissance du joueur (JJMMAAAA) : ")
    return player_birthdate
    
def get_player_gender():
    player_gender = input("Veuillez saisir le genre du joueur (M ou F) : ")
    return player_gender

def get_player_elo():
    player_elo = input("Veuillez saisir le classement du joueur ")
    return player_elo