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
    print('Started!')
    print(pomodoro.time)
    while True:
        timedelta = datetime.now(tz=None) - pomodoro.time
        if timedelta.total_seconds() % 60 == 0:
            print(f'{int(timedelta.total_seconds()//60)} minutes has elapsed.')
        if timedelta.total_seconds() == 1500:
            print('Time over!')
            return False


def main():
    pomodoro_start()


if __name__ == '__main__':
    exit(main())
