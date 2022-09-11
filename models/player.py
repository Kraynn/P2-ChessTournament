class Player:
    """ Classe qui instancie un joueur et crée un dictionnaire
    """

    def __init__(self, data):
        self.name = data["Nom"]
        self.first_name = data["Prenom"]
        self.birthdate = data["Date de naissance"]
        self.gender = data["Genre"]
        self.elo = int(data["Classement"])
       
    def serialize(self):
        serialized_player = {
            "Nom": self.name,
            "Prenom": self.first_name,
            "Date de naissance": self.birthdate,
            "Genre": self.gender,
            "Classement": self.elo,
        }
        return serialized_player

