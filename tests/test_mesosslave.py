import json
import types

import pytest

from marathon.models.constraint import MarathonConstraint

from ucrspawner import mesosslave
from ucrspawner.exceptions import UCRSpawnerException

def test_match(monkeypatch):
    mesos_master_response = json.loads('{"id":"40237088-f509-46a4-a5f1-c8f88ca8e03f-S0","hostname":"mesos-slave","port":5051,"attributes":{"foo":123.0,"bar":"wow"},"pid":"slave(1)@172.24.0.5:5051","registered_time":1518339392.10703,"resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"used_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":0.0},"offered_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":0.0},"reserved_resources":{},"unreserved_resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"active":true,"version":"1.4.0","capabilities":["MULTI_ROLE","HIERARCHICAL_ROLE","RESERVATION_REFINEMENT"],"reserved_resources_full":{},"unreserved_resources_full":[{"name":"cpus","type":"SCALAR","scalar":{"value":2.0},"role":"*"},{"name":"mem","type":"SCALAR","scalar":{"value":999.0},"role":"*"},{"name":"disk","type":"SCALAR","scalar":{"value":69716.0},"role":"*"},{"name":"ports","type":"RANGES","ranges":{"range":[{"begin":31000,"end":32000}]},"role":"*"}],"used_resources_full":[],"offered_resources_full":[]}')

    slave = mesosslave.MesosSlave(mesos_master_response)

    assert slave.match(MarathonConstraint('foo', 'LIKE', '123'))
    assert not slave.match(MarathonConstraint('foo', 'UNLIKE', '123'))
    assert slave.match(MarathonConstraint('bar', 'LIKE', 'wo[w]'))
    assert not slave.match(MarathonConstraint('bar', 'LIKE', 'wof'))
    assert not slave.match(MarathonConstraint('unknown', 'LIKE', 'hoge'))
    assert slave.match(MarathonConstraint('unknown', 'UNLIKE', 'hoge'))
    with pytest.raises(UCRSpawnerException) as excinfo:
        slave.match(MarathonConstraint('foo', 'UNKNOWN', ''))
    assert str(excinfo.value) == 'Unsupported constraint operator: UNKNOWN'
