from datetime import datetime

from freezegun import freeze_time

import pomodoro.pomodoro


@freeze_time('2020-8-15 12:00:00', auto_tick_seconds=1500)
def test_initial_timer_start():
    pomo = pomodoro.pomodoro._pomodoro(0, datetime.now())
    pomodoro.pomodoro.pomodoro_run(pomo)
    assert pomo.break_count == 5
