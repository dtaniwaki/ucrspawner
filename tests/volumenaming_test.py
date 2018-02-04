import types
import pytest
from jupyterhub.spawner import Spawner
from ucrspawner import volumenaming


def test_default_format_volume_name(monkeypatch):
    spawner = Spawner(user=types.SimpleNamespace(name='bar', state={}))
    assert volumenaming.default_format_volume_name('foo-{username}', spawner), 'foo-bar'
    assert volumenaming.default_format_volume_name('foo-{username}/{username}', spawner), 'foo-bar/bar'
