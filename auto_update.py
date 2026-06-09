import datetime

with open("update_log.txt", "a") as f:
    f.write(f"Updated on: {datetime.datetime.now()}\n")