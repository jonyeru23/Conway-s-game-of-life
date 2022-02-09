import pytest
from game import *

@pytest.fixture(scope="module")
def objects():
    objects = {
        'game': PyGame(),
        'board': Board(PyGame().screen),
    }
    objects['game'].set_up()
    yield objects


def test_set_up_game(objects):
    assert objects['game'].is_running() is True


def test_terminate(objects):
    objects['game'].terminate()
    assert objects['game'].is_running() is False


def test_update_board(objects):
    assert objects['board'].update_screen() is None




