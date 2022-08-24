from models.match import Match

class Round:
    """ Classe qui instancie une manche et crée un dictionnaire
    """

    def __init__(self, number, date, start, end, matchs):
        self.number = number
        self.date = date
        self.start = start
        self.end = end
        self.matchs = matchs

    def serialize(self):
        serialized_round = {
            "Numero de manche": self.number,
            "Date": self.date,
            "Heure de dbut": self.start,
            "Heure de fin": self.end,
            "Matchs": self.matchs
        }
        return serialized_round

        