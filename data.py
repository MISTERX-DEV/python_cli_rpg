with( open ("Data/message/Actions.txt", "r", encoding="utf-8") as file_action,
      open ("Data/message/History.txt", "r", encoding="utf-8") as file_history):
    action_TEXT = file_action.read()
    