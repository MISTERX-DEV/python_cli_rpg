import json
import sqlite3



def init_db():
    conn = sqlite3.connect("Data/DataBase.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        level INTEGER,
        health INTEGER
    )
    """)
    conn.commit()
    conn.close()




with( open ("Data/message/Actions.txt", "r", encoding="utf-8") as file_action,
      open ("Data/message/History.txt", "r", encoding="utf-8") as file_history):
    action_TEXT = file_action.read()




with( open ("Data/message/Actions.txt", "r", encoding="utf-8") as file_action,
      open ("Data/message/History.txt", "r", encoding="utf-8") as file_history):
    action_TEXT = file_action.read()















def open_json(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)




player_json = {
    "name": "Hero",
    "level": 1,
    "health": 100,
    "inventory": []
}



#save_json("player.json", player_json)
#print(open_json("player.json"))