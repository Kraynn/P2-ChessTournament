from models.match import Match

class Round:
    """ Classe qui instancie une manche et crée un dictionnaire
    """

    def __init__(self, number, date, start, end):
        self.number = number
        self.date = date
        self.start = start
        self.end = end
        self.matchs = []

    def serialize(self):
        serialized_round = {
            "Numéro de manche": self.number,
            "Date": self.date,
            "Heure de début": self.start,
            "Heure de fin": self.end,
            "Matchs": self.matchs
        }
        return serialized_round

    def add_match(self, player_1, player_2):
        """ Ajoute un match au round """
        match = Match(player_1, player_2)
        self.matchs.append(match)
        