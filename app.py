import data
import random
import os
from log import *


cls = lambda: os.system('clear')

player_default = {
    "name":"Player",
    "class":"none",
    "health":20,
    "steps":3,
    "level":1,
    "xp":0,
    "charactetistics":{
        "health_c":20,
        "stamina_c":3,
        "strength_c":5,
        "dexterity_c":5
        
    },
    "equipment":{
        "weapon":data.get_item_by_id(1),
        "armor":"none",
        "potions":"none"
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
    print(f'\nХарактеристики игрока: \nЗдоровье: [ {player["health"]} ] \nВыносливость: [ {player["steps"]} ] \nОружие: {player["equipment"]["weapon"][1]} | ATK: {player["equipment"]["weapon"][3]} | ACR: {player["equipment"]["weapon"][4]}')






def fight():
    cls() # ------------------УБРАТЬ СКОРЕЕ ВСЕГО!!!----<----<---<--<--<-<-<-<-
    while player["health"] > 0:
        view_monstro(monster)
        view_player_characteristics(player)
        action = int(input("\nВыберите ваши действия:\n[1] Атака\n[2] Попущен\n------> "))
        player_hit_chance = random.randint(1, 100)
        monster_hit_chance = random.randint(1, 100)


        if action == 1:
            if player_hit_chance <= player["equipment"]["weapon"][4]:
                monster["health"] -= player["equipment"]["weapon"][3]
                cls()
                print(f"Вы нанесли {player["equipment"]["weapon"][3]} урона!")
            else:
                cls()
                print("Вы промахнулись!")
        elif action == 2:
            if monster_hit_chance <= monster["accurancy"]:
                player["health"] -= monster["attack_power"]
                cls()
                print(f"Монстр нанес вам {monster['attack_power']} урона!")
            else:
                cls()
                print("Монстр промахнулся!")
        else:
            cls()
            print("Ты дурачок?")
            player["health"] -= 1000
    else:
        print("Вы отсосали, идите отсудя >:)")



def kill_monster():
    player["xp"] += monster["xp"]

def level_up():
    view_player_characteristics(player)
    level = 1
    skill_point = 0
    while True:
        dev_act = int(input("[1] Выдать XP\n[2] Прокачка\nДействие: "))
        if dev_act == 1:
            num = int(input("XP: "))
            player["xp"] += num
        elif dev_act == 2 and skill_point != 0:
            view_player_characteristics(player)
            action = int(input("\nПрокачать\n[1] Здоровье\n[2] Стамина\n[3] Сила\n[4] Ловкость\nДействие: "))
            if action == 1:
                player["health_c"] += 1
                skill_point -= 1
            elif action == 2:
                player["stamina_c"] += 1
                skill_point -= 1
            elif action == 3:
                player["strength_c"] += 1
                skill_point -= 1
            elif action == 4:
                player["dexterity_c"] += 1
                skill_point -= 1
        else:
            print("Нету поинтов")
        

        if num >= 100:
            num -= 100
            level += 1
            skill_point += 1

def boss():
    pass






# Вызов
#fight()
level_up()



