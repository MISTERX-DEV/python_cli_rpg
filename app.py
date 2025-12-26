import data
import random
import os


cls = lambda: os.system('clear')

player_default = {
    "name":"Player",
    "class":"none",
    "steps":3,
    "hp":20,
    "power":5,
    "accurancy":70,
    "skill":1,
    "xp":0,
    "charactetistics":{
        
    },
    "inventory":[]
    }





'''

[ 1 Монстр ] [ 2 Монстр ] [ 3 Монстр ]
  [ HP:1 ]     [ HP:2 ]     [ HP:3 ]
 [ ATK: 3 ]   [ ATK: 2 ]   [ ATK: 1 ]

Характеристики игрока
Здоровье: 4
Выносливость: 4
Сила (ака оружие): 2 , требует 2

Серия атак: 2,1,3
Серия атак игрока: Удар, Уклоение, пропуск

'''

def init_game():
    #data.create_player("player_test.json", player_default)
    player = data.load_player("player_test.json")
    monster = {
        "id": data.get_monster_by_id(1)[0],
        "name": data.get_monster_by_id(1)[1],
        "desc": data.get_monster_by_id(1)[2],
        "health": data.get_monster_by_id(1)[3],
        "attack_power": data.get_monster_by_id(1)[4],
        "accurancy": data.get_monster_by_id(1)[5],
        "xp": data.get_monster_by_id(1)[6]
    }
    return [player, monster]

player = init_game()[0]
monster = init_game()[1]


def view_monstro(monster):
    print(f''' [ {monster["name"]} ] \n [ HP:{monster["health"]} ] \n [ ATK:{monster["attack_power"]} ] \n [ ACR:{monster["accurancy"]} ]''')
def view_player_characteristics(player):
    print(f'''\nХарактеристики игрока: \nЗдоровье:{player["hp"]} \nшанс:{player["accurancy"]} \nСила:{player["power"]}''')











while player["hp"] >= 0:
    cls()
    view_monstro(monster)
    view_player_characteristics(player)
    action = int(input("\nВыберите ваши действия:\n[1] Атака\n[2] Попущен\n------> "))
    if action == 1:
        monster["health"] -= player["power"]
    elif action == 2:
        player["hp"] -= monster["attack_power"]
    else:
        print("Ты дурачок?")
        player["hp"] -= 1000

else:
    print("Вы отсосали, идите отсудя >:)")











