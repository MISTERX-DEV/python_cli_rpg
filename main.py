import data
import app
import log

player_name = "player_test"+".json"

def main():
    try:
        data.init_db()
        app.init_game()
    finally:
        data.conn.close()
if __name__ == "__main__":
    main()
    print("Start game!")
    log.log("Start game!")