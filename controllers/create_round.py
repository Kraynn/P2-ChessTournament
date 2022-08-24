from tinydb import TinyDB, Query
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from models.player import Player
import views.v_add_player as vp 
import views.v_round as vr
import views.v_tournament as vt

def takeFirst(elem):
    return elem[0]

def takeSecond(elem):
    return elem[1]

def start_round(tournoi):
    db = TinyDB("db.json")
    User = Query()
    tn_table = db.table("Tournois")
    # current_tournament = tn_table.search(User.Titre == "f{tournoi}")
    tournoi = tournoi
    round_number = vr.get_round_number()
    round_date = vr.get_round_date()
    round_start = vr.get_round_start()
    round_end = vr.get_round_end()                                                    # a voir si on crée pas une fonction apart pour cloturer le round
    if tn_table.search(User.Titre==f"{tournoi}")[0]["Player_Score"] == []:
        matches = first_round_matches(tournoi)
    else:
        matches = next_round_matches(tournoi)
    round = Round(round_number, round_date, round_start, round_end, matches)
    serialized_round = round.serialize()
    tn_table.upsert({"Manches": serialized_round}, User.Titre ==f"{tournoi}")              #Bug pour ajouter multiple round meme si le score s'update bien

def get_match_score(player_1,player_2):
    score = input(f"Si {player_1} a gagné : tapez 1 \n Si {player_2} a gagné : tapez 2 \n  Si match nul : tapez 3")
    if score == "1":
        return 1, 0
    elif score == "2":
        return 0, 1
    elif score == "3":
        return 0.5, 0.5

def first_round_matches(tournoi):
    db = TinyDB("db.json")
    players_table = db.table("Joueurs")
    tn_table = db.table("Tournois")
    User=Query()

    for player in players_table:
        x = tn_table.search(User.Titre == f"{tournoi}")[0]              
        y = x["Joueurs"]
    players = [x for x in players_table if x.doc_id in y]
    playerModels = [Player(x) for x in players]
    playerModels.sort(key=lambda k: k.elo)
    
    player_score = []
    serialized_matches = []        
    for i in range(4):
        result_1, result_2 = get_match_score(playerModels[i].name, playerModels[4+i].name)
        match = Match(playerModels[i].name, result_1, playerModels[4+i].name, result_2)
        serialized_match = match.serialize()
        serialized_matches.append(serialized_match)
        z = [playerModels[i].name, result_1]
        player_score.append(z)
        y = [playerModels[4+i].name, result_2]
        player_score.append(y)
    player_score.sort(key=takeSecond,  reverse=True)
    tn_table.upsert({"Player_Score": player_score}, User.Titre==f"{tournoi}")
    return serialized_matches

def next_round_matches(tournoi):
    db = TinyDB("db.json")
    tn_table = db.table("Tournois")
    User=Query()
    
    player_score = tn_table.search(User.Titre==f"{tournoi}")[0]["Player_Score"]
    player_score_updated = []
    players = []
    score = []
    serialized_matches = []                    
    for i in range(8):
        players.append(takeFirst(player_score[0+i]))
        score.append(takeSecond(player_score[0+i]))
    for i in range(4):
        result_1, result_2 = get_match_score(players[i], players[i+1])
        match = Match(players[i], result_1, players[1], result_2)
        serialized_match = match.serialize()
        serialized_matches.append(serialized_match)
        match_J1 = [players[i], result_1 + score[i]]
        match_J2 = [players[i+1], result_2 + score[i+1]]
        players.pop(0)
        score.pop(0)
        player_score_updated.append(match_J1)
        player_score_updated.append(match_J2)
    player_score_updated.sort(key=takeSecond,  reverse=True)
    tn_table.update({"Player_Score": player_score_updated}, User.Titre==f"{tournoi}") 
    return serialized_matches 