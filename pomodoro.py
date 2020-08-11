from datetime import datetime


class _pomodoro:
    def __init__(self, count=0, time=0):
        self.count = count

    def get_count(self) -> int:
        return self.count

    def start_timer(self) -> None:
        self.time = datetime.now(tz=None)


def main():
    pomodoro = _pomodoro()
    pomodoro.count += 1
    print(pomodoro.get_count())


if __name__ == '__main__':
    exit(main())
