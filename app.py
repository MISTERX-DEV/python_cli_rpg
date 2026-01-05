import main
import menu
import data
import random
import os
from log import *


cls = lambda: os.system('clear')

player_default = {
    "name":"Player",
    "class":"none",
    "health":0,
    "stamina":0,
    "level":1,
    "xp":0,
    "characteristics":{
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
    #data.create_player(main.player_name, player_default)
    updating_the_characteristics()

player = data.load_player(main.player_name)
monster_data = data.get_monster_by_id(1)
monster = {
        "id": monster_data[0],
        "name": monster_data[1],
        "desc": monster_data[2],
        "health": monster_data[3],
        "attack_power": monster_data[4],
        "accuracy": monster_data[5],
        "xp": monster_data[6]
    }



def sex():
    print("Вы выбрали атаку! SEX")

def fight():
    cls() # ------------------УБРАТЬ СКОРЕЕ ВСЕГО!!!----<----<---<--<--<-<-<-<-
    while player["health"] > 0:
        menu.show_monster(monster)
        menu.show_player_characteristics(player)
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
            if monster_hit_chance <= monster["accuracy"]:
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

def level_up(player):

    while True:
        action = int(input("\n[1] Повысить xp\n[2] Повысить уровень\n------> "))
        if action == 1:
            player["xp"] = int(input("Введите количество xp: "))
        elif action == 2:
            if player["xp"] >= 100:
                player["level"] += 1
                player["xp"] -= 100
                player["characteristics"]["health_c"] += 1
                player["characteristics"]["stamina_c"] += 1
                player["characteristics"]["strength_c"] += 1
                player["characteristics"]["dexterity_c"] += 1
                print("Поздравляем! Вы повысили уровень!")
                updating_the_characteristics()
                menu.show_player_characteristics(player)
                

def updating_the_characteristics():
    player["health"] = player["characteristics"]["health_c"]
    player["stamina"] = player["characteristics"]["stamina_c"]
    data.save_player(main.player_name, player)

def boss():
    pass






# Вызов
#fight()
#level_up(player)



