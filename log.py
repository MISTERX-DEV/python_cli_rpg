import datetime
def log(obj):
    with open("log.txt", 'a') as file:
        file.write(f"[{datetime.datetime.now()}][LOG][GAME][STABLE] {obj}\n")
def log_er(obj):
    with open("log.txt", 'a') as file:
        file.write(f"[LOG][GAME][ERROR] {obj}\n")
def log_out(obj):
    with open("log.txt", 'a') as file:
        file.write(f"[LOG][UNGAME] {obj}\n")