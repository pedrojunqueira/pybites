import pytest

from workouts import print_workout_days


@pytest.mark.parametrize('workout, day', [('upper body #1', 'mon\n'),
                           ('lower body #1', 'tue\n'),
                           ('30 min cardio', 'wed\n'),
                           ('upper body #2', 'thu\n'),
                           ('lower body #2', 'fri\n'),
                            ])
def test_print_workout_days(capsys, workout, day):
    print_workout_days(workout)
    captured = capsys.readouterr()
    assert captured.out == day.title()



