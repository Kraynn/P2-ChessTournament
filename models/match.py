class Match:
    """Classe qui instancie match et crée un dictionnaire
    """

    def __init__(self, player_1, player_2, result_p1, result_p2):
        self.p1 = player_1
        self.p2 = player_2
        self.result_p1 = result_p1
        self.result_p2 = result_p2
        self.serialized_match = []

    def serialize(self):
        serialized_match = {
            "Player1": self.p1,
            "Score1": self.result_p1,
            "Player2": self.p2,
            "Score2": self.result_p2,
        }
        return serialized_match
