import types

from jupyterhub.spawner import Spawner

from ucrspawner import utils


def test_remove_zeros(monkeypatch):
    assert utils.remove_zeros(123) == '123'
    assert utils.remove_zeros(123.0) == '123'
    assert utils.remove_zeros(123.1) == '123.1'
