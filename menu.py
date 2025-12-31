def show_monster(monster):
    print(f''' [ {monster["name"]} ] \n [ HP:{monster["health"]} ] \n [ ATK:{monster["attack_power"]} ] \n [ ACR:{monster["accuracy"]} ]''')

def show_player_characteristics(player):
    print(f'\nХарактеристики игрока: \nЗдоровье: [ {player["health"]} ] \nВыносливость: [ {player["stamina"]} ] \nОружие: {player["equipment"]["weapon"][1]} | ATK: {player["equipment"]["weapon"][3]} | ACR: {player["equipment"]["weapon"][4]}')

def show_main_menu():
    pass