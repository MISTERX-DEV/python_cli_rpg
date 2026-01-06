import data
import app
import log
import menu

player_name = "player_test"+".json"

def main():
    try:
        data.init_db()  
        app.init_game()
        while True:
            menu.handle_actions(menu.debug_menu(), input("Enter your choice: "))
    finally:
        data.conn.close()
if __name__ == "__main__":
    main()