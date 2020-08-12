import pomodoro


def test_initial_timer_start():
    test = pomodoro.pomodoro_start()
    assert test is False
