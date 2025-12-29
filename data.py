import json
import sqlite3


def init_db(): 
    conn = sqlite3.connect("Data/DataBase.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        attack_power INTEGER,
        accuracy INTEGER,
        required_strength INTEGER,
        required_dexterity INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS monsters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        health INTEGER,
        attack_power INTEGER,
        accuracy INTEGER,
        xp INTEGER,
        item_drop INTEGER
    )
    ''')
    conn.commit()
    #conn.close()
    return conn, cursor
conn, cursor = init_db()

# Предметы
def get_all_items():
    cursor.execute('SELECT * FROM items')
    return cursor.fetchall()

def get_item_by_id(item_id):
    cursor.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    return cursor.fetchone()

def get_item_by_name(item_name):
    cursor.execute('SELECT * FROM items WHERE name = ?', (item_name,))
    return cursor.fetchone()

# Монстры
def get_all_monsters():
    cursor.execute('SELECT * FROM monsters')
    return cursor.fetchall()

def get_monster_by_id(monster_id):
    cursor.execute('SELECT * FROM monsters WHERE id = ?', (monster_id,))
    return cursor.fetchone()

def get_monster_by_name(monster_name):
    cursor.execute('SELECT * FROM monsters WHERE name = ?', (monster_name,))
    return cursor.fetchone()




def load_player(file:str):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def create_player(file:str, data:dict):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)



# НЕ ТРОГАТЬ!!
'''with(
    open('Data/message/Inscriptions.txt', 'r', encoding='utf-8') as inscription_file,
    open('Data/message/Trader.txt', 'r', encoding='utf-8') as trader_file,
    open('Data/message/History.txt', 'r', encoding='utf-8') as history_file,
    open('Data/message/MainMenu.txt', 'r', encoding='utf-8') as mainmenu_file,
    open('Data/message/Tips.txt', 'r', encoding='utf-8') as tips_file,
    open('Data/message/Actions.txt', 'r', encoding='utf-8') as actions_file
    ):
    trader_text = trader_file.readlines()
    inscription_text = inscription_file.readlines()
    history_text = history_file.readlines()
    mainmenu_text = mainmenu_file.readlines()
    tips_text = tips_file.readlines()
    actions_text = actions_file.readlines()'''

with( open ("Data/message/Actions.txt", "r", encoding="utf-8") as file_action,
      open ("Data/message/History.txt", "r", encoding="utf-8") as file_history):
    action_TEXT = file_action.read()