import app
import time

def show_monster(monster):
    print(f''' [ {monster["name"]} ] \n [ HP:{monster["health"]} ] \n [ ATK:{monster["attack_power"]} ] \n [ ACR:{monster["accuracy"]} ]''')

def show_player_characteristics(player):
    print(f'\nХарактеристики игрока: \nЗдоровье: [ {player["health"]} ] \nВыносливость: [ {player["stamina"]} ] \nОружие: {player["equipment"]["weapon"][1]} | ATK: {player["equipment"]["weapon"][3]} | ACR: {player["equipment"]["weapon"][4]}')

def printable_animation(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()



def show_main_menu():
    print('[1] Начать игру\n[2] Загрузить игру\n[0] Выйти из игры')

    actions = {
        "1": "Начинаем новую игру!",
        "2": "Загружаем игру!"
    }
    
    return actions

def debug_menu():
    print('\n=== Debug Menu ===')
    print('[1] Показать характеристики игрока')
    print('[2] Показать текущее оружие игрока')
    print('[3] Обновить характеристики игрока')
    print('[4] Показать монстра')
    print('[5] Начать бой с монстром')

    actions = {
        "1": lambda: show_player_characteristics(app.player),
        "2": lambda: print(f'Оружие игрока: {app.player["equipment"]["weapon"][1]} | ATK: {app.player["equipment"]["weapon"][3]} | ACR: {app.player["equipment"]["weapon"][4]}'),
        "3": lambda: app.update_player_characteristics(),
        "4": lambda: show_monster(app.monster),
        "5": lambda: app.fight()
    }
    return actions




def handle_actions(actions_menu, choice):
    for actions in actions_menu:
        if str(choice) in actions:
            if callable(actions_menu[actions]):
                actions_menu[actions]()
                break
            else:
                print(actions_menu[actions])
                break
    else:
        print("Invalid choice. Try again.")
        return True





def main(current_menu, choice):
    running = True
    while running:
        running = handle_actions(current_menu, choice)