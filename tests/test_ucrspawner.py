import types

import pytest

from marathon.models.constraint import MarathonConstraint

from ucrspawner import UCRSpawner
from ucrspawner.exceptions import UCRSpawnerException


def test_get_constraints(monkeypatch):
    spawner = UCRSpawner(user=types.SimpleNamespace(name='bar', state={}))
    spawner.marathon_constraints = [['foo', 'LIKE', 'bar'], ['bar', 'UNLIKE', 'foo']]
    assert spawner.get_constraints() == [MarathonConstraint('foo', 'LIKE', 'bar'), MarathonConstraint('bar', 'UNLIKE', 'foo')]
    with pytest.raises(UCRSpawnerException) as excinfo:
        spawner.marathon_constraints = [['foo', 'UNKNOWN', 'bar'], ['bar', 'UNKNOWN', 'foo'], ['bar', 'SAME', 'bar']]
        spawner.get_constraints()
    assert str(excinfo.value) == "Unsupported constraint operators: ['SAME', 'UNKNOWN']"
