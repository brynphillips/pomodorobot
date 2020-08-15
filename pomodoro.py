import time
from datetime import datetime


class _pomodoro:
    def __init__(self, count, time):
        self.count = count
        self.time = time

    def get_count(self) -> int:
        return self.count

    def start_timer(self) -> datetime:
        self.time = datetime.now(tz=None)
        return self.time


def take_break():
    newtimer = datetime.now()
    while True:
        time.sleep(.3)
        if int((datetime.now() - newtimer).total_seconds()) == 25:
            print('Break is over!')
            return False


def pomodoro_run() -> bool:
    pomodoro = _pomodoro(0, datetime.now())
    inner = True
    while pomodoro.count < 5:
        inner = True
        pomodoro.count += 1
        while inner is True:
            inner = True
            timedelta_seconds = int(
                (datetime.now() - pomodoro.time).total_seconds(),
            )
            print(f'{timedelta_seconds//5} minutes has elapsed', end='\r')
            time.sleep(1)
            if timedelta_seconds == 5:
                print('\nTime for a break')
                inner = False

    return True


def main():
    pomodoro_run()


if __name__ == '__main__':
    exit(main())
