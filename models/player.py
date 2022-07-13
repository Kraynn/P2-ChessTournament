class Player:
    """ Classe qui instancie un joueur et crée un dictionnaire
    """

    def __init__(self, name, first_name, birthdate, gender, elo):
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo

    def serialize(self):
        serialized_player = {
            "Nom": self.name,
            "Prénom": self.first_name,
            "Date de naissance": self.birthdate,
            "Genre": self.gender,
            "Classement": self.elo
        }
        return serialized_player