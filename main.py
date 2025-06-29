import time
from plyer import notification

while True:
    # print("Hey, drink a little water.")
    notification.notify(title = "Reminder", message = "Hey, drink a little water.")
    time.sleep(3600)


