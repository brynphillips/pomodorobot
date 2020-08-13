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


def pomodoro_start() -> bool:
    pomodoro = _pomodoro(0, datetime.now())
    pomodoro.count += 1
    pomodoro.start_timer
    if pomodoro.count < 5:
        print('Started!')
    print(pomodoro.time)
    while True and pomodoro.count < 4:
        timedelta = datetime.now(tz=None) - pomodoro.time
        if int(timedelta.total_seconds()) % 60 == 0:
            print(
                f'{int(timedelta.total_seconds()//60)} minutes has lapsed.',
                end='\r',
            )
        time.sleep(
            0.3,
        )
        # TODO: Need to figure out the loop for the 4 sessions of workings
        if int(timedelta.total_seconds()) == 1500 and pomodoro.count < 4:
            return False

        # TODO: This is for the big break.
        if pomodoro.count == 4:
            pomodoro.count = 0
            print('Time to take a 25 minute break! Good job! Keep it up!')
            timedelta = datetime.now(tz=None) - pomodoro.time
            if int(timedelta.total_seconds()) == 1500:
                print('Break is over!')
                return False
    return True


def main():
    pomodoro_start()


if __name__ == '__main__':
    exit(main())
