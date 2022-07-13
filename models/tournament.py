class Tournament:
    """Classe qui instancie un tournoi et crée un dictionaire
    """
    def __init__(self, title, location, date, game_mode, description, nb_of_rounds=4):
        self.title = title
        self.location = location
        self.date = date                                           # Voir library datetime pour format
        self.nb_of_rounds = nb_of_rounds
        self.game_mode = game_mode
        self.description = description
        self.rounds = []
        self.players = []

    def serialize(self):
        serialized_tournament = {
            "Titre": self.title,
            "Lieu": self.location,
            "Date": self.date,
            "Mode de jeu": self.game_mode,
            "Description": self.description,
            "Nombre de manches": self.nb_of_rounds,
            "Joueurs" : self.players,
            "Manches": self.rounds
        }
        return serialized_tournament

    def add_player(self, player):
        """ Ajoute un joueur au tournoi"""
        self.players.append(player)

    def add_round(self, round):
        """ Ajoute une manche au tournoi"""
        self.rounds.append(round)