import data

if __name__ == "__main__":
    print("Start game!")
    data.init_db()
    print(data.get_all_items())