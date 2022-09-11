class Match:
    """Classe qui instancie un match et crée un dictionnaire
    """

    def __init__(self, player_1, result_p1, player_2, result_p2):
        self.player_1 = player_1
        self.result_p1 = int(result_p1)
        self.player_2 = player_2
        self.result_p2 = int(result_p2)
    
    # def serialize(self):
    #      serialized_match = {
    #          "Player1": self.player_1,
    #          "Score1": self.result_p1,
    #          "Player2": self.player_2,
    #          "Score2": self.result_p2,
    #      }
    #      return serialized_match

    def serialize(self):
        serialized_match = (
            [self.player_1, self.result_p1],
            [self.player_2, self.result_p2]
        )
        return serialized_match