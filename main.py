import data
import app
import log
import menu

player_name = "player_test"+".json"

def main():
    try:
        data.init_db()
        app.init_game()
        menu.main(menu.show_fight_menu(), input("Choose an action: "))
    finally:
        data.conn.close()
if __name__ == "__main__":
    main()
    print("Start game!")
    log.log("Start game!")