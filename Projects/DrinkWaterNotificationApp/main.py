import time
from plyer import notification

while True:
    print("Please sip some water!")
    notification.notify(title="Please drink some water",
                        message = "You need to drink some water",timeout=5)
    time.sleep(10)