import time
from plyer import notification


def nt():
    time.sleep(1500)
    while True:
        notification.notify(
            title="Please take a break",
            message="It's good to take short break after 25 minutes of work (as per the Pomodoro Techniqe)",
            timeout=10
        )
        time.sleep(1500)


nt()
