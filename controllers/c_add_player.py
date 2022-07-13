import views.v_add_player as vp
from models.player import Player

# def add_player():
#     player = Player(name=add_player_info(0), 
#     first_name=add_player_info(1),
#     birthdate=add_player_info(2),
#     gender=add_player_info(3),
#     elo=add_player_info(4)
#     )
#     serialized_player = player.serialize()
#     print(serialized_player)

def add_player():
    name = vp.get_player_name()
    firstname = vp.get_player_firstname()
    birthdate = vp.get_player_birthdate()
    gender = vp.get_player_gender()
    ranking = vp.get_player_elo()
    player = Player(name, firstname, birthdate, gender, ranking)
    serialized_player = player.serialize()

    print(serialized_player)

add_player()