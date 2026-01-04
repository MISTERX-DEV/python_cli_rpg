def show_monster(monster):
    print(f''' [ {monster["name"]} ] \n [ HP:{monster["health"]} ] \n [ ATK:{monster["attack_power"]} ] \n [ ACR:{monster["accuracy"]} ]''')

def show_player_characteristics(player):
    print(f'\nХарактеристики игрока: \nЗдоровье: [ {player["health"]} ] \nВыносливость: [ {player["stamina"]} ] \nОружие: {player["equipment"]["weapon"][1]} | ATK: {player["equipment"]["weapon"][3]} | ACR: {player["equipment"]["weapon"][4]}')

def show_main_menu():
    print('[1] Начать игру\n[2] Загрузить игру\n[0] Выйти из игры')

    actions = {
        "1": "Начинаем новую игру!",
        "2": "Загружаем игру!"
    }
    
    return actions

def show_fight_menu():
    print('[1] Атаковать\n[2] Защищаться\n[3] Использовать предмет\n[4] Сбежать\n[5] Проверить характеристики\n[0] Выйти из боя')

    actions = {
        "1": "Вы выбрали атаку!",
        "2": "Вы защищаетесь!",
        "3": "Вы используете предмет!",
        "4": "Вы сбегаете!",
        "5": "Показ характеристик...",
        "0": "Выход из боя..."
    }
    
    return actions









def handle_actions(choice, actions_menu):
    for i in actions_menu:
        if str(choice) == i:
            if callable(actions_menu[i]):
                actions_menu[i]()
            else:
                print(actions_menu[i])
        
choice = 1


def main(current_menu):
    while True:
        handle_actions(choice, current_menu)
        input("Нажмите Enter чтобы продолжить...")

if __name__ == "__main__":
    main(show_main_menu())