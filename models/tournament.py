class Tournament:
    """Classe qui instancie un tournoi et crée un dictionaire
    """
    def __init__(self, title, location, date, game_mode, description, nb_of_rounds):
        self.title = title
        self.location = location
        self.date = date                                           # Voir library datetime pour format
        self.nb_of_rounds = nb_of_rounds
        self.game_mode = game_mode
        self.description = description
        self.rounds = []
        self.players = []
        self.player_score = []
        


    def serialize(self):
        serialized_tournament = {
            "Titre": self.title,
            "Lieu": self.location,
            "Date": self.date,
            "Mode de jeu": self.game_mode,
            "Description": self.description,
            "Nombre de manches": self.nb_of_rounds,
            "Joueurs" : self.players,
            "Player_Score": self.player_score,
            "Manches": self.rounds,
        }
        return serialized_tournament
