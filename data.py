import json




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