from datetime import datetime

import pomodoro


def test_initial_timer_start():
    pomo = pomodoro._pomodoro()
    pomo.start_timer()
    assert isinstance(pomo.time, datetime)
