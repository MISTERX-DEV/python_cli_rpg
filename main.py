import data
import app
import log

player_name = "player_test"+".json"

def main():
    data.init_db()
    app.init_game()

if __name__ == "__main__":
    main()
    print("Start game!")
    log.log("Start game!")