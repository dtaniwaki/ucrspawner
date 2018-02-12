import json
import types

import pytest

from marathon.models.constraint import MarathonConstraint

from ucrspawner import mesosslave
from ucrspawner.exceptions import UCRSpawnerException

def test_match(monkeypatch):
    mesos_master_response = json.loads('{"id":"40237088-f509-46a4-a5f1-c8f88ca8e03f-S0","hostname":"mesos-slave","port":5051,"attributes":{"int":123,"int-float":123.0,"float":123.1,"text":"wow","keys":"[1000-1500]","sets":"{\\"a\\",\\"b\\",\\"c\\"}"},"pid":"slave(1)@172.24.0.5:5051","registered_time":1518339392.10703,"resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"used_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":0.0},"offered_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":0.0},"reserved_resources":{},"unreserved_resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"active":true,"version":"1.4.0","capabilities":["MULTI_ROLE","HIERARCHICAL_ROLE","RESERVATION_REFINEMENT"],"reserved_resources_full":{},"unreserved_resources_full":[{"name":"cpus","type":"SCALAR","scalar":{"value":2.0},"role":"*"},{"name":"mem","type":"SCALAR","scalar":{"value":999.0},"role":"*"},{"name":"disk","type":"SCALAR","scalar":{"value":69716.0},"role":"*"},{"name":"ports","type":"RANGES","ranges":{"range":[{"begin":31000,"end":32000}]},"role":"*"}],"used_resources_full":[],"offered_resources_full":[]}')

    slave = mesosslave.MesosSlave(mesos_master_response)

    # Int
    assert slave.match(MarathonConstraint('int', 'LIKE', '123'))
    assert not slave.match(MarathonConstraint('int', 'LIKE', '124'))
    assert not slave.match(MarathonConstraint('int', 'UNLIKE', '123'))
    assert slave.match(MarathonConstraint('int', 'UNLIKE', '124'))

    # Int-Float
    assert slave.match(MarathonConstraint('int-float', 'LIKE', '123'))
    assert not slave.match(MarathonConstraint('int-float', 'LIKE', '124'))
    assert not slave.match(MarathonConstraint('int-float', 'UNLIKE', '123'))
    assert slave.match(MarathonConstraint('int-float', 'UNLIKE', '124'))

    # Float
    assert slave.match(MarathonConstraint('float', 'LIKE', '123.1'))
    assert not slave.match(MarathonConstraint('float', 'LIKE', '124.1'))
    assert not slave.match(MarathonConstraint('float', 'UNLIKE', '123.1'))
    assert slave.match(MarathonConstraint('float', 'UNLIKE', '124.1'))

    # Text
    assert slave.match(MarathonConstraint('text', 'LIKE', 'wow'))
    assert slave.match(MarathonConstraint('text', 'LIKE', 'wo[w]'))
    assert not slave.match(MarathonConstraint('text', 'LIKE', 'wof'))
    assert not slave.match(MarathonConstraint('text', 'UNLIKE', 'wow'))
    assert not slave.match(MarathonConstraint('text', 'UNLIKE', 'wo[w]'))
    assert slave.match(MarathonConstraint('text', 'UNLIKE', 'wof'))

    # Ignore range and set attributes
    assert not slave.match(MarathonConstraint('keys', 'LIKE', '1000'))
    assert not slave.match(MarathonConstraint('keys', 'UNLIKE', '1000'))
    assert not slave.match(MarathonConstraint('sets', 'LIKE', 'a'))
    assert not slave.match(MarathonConstraint('sets', 'UNLIKE', 'a'))

    # Unknown fields
    assert not slave.match(MarathonConstraint('unknown', 'LIKE', 'hoge'))
    assert slave.match(MarathonConstraint('unknown', 'UNLIKE', 'hoge'))


    # Invalid cases
    with pytest.raises(UCRSpawnerException) as excinfo:
        slave.match(MarathonConstraint('foo', 'LIKE', 123))
    assert str(excinfo.value) == "Unsupported constraint value type: <class 'int'>"
    with pytest.raises(UCRSpawnerException) as excinfo:
        slave.match(MarathonConstraint('foo', 'UNKNOWN', ''))
    assert str(excinfo.value) == 'Unsupported constraint operator: UNKNOWN'

def test_is_available(monkeypatch):
    mesos_master_response = json.loads('{"id":"40237088-f509-46a4-a5f1-c8f88ca8e03f-S0","hostname":"mesos-slave","port":5051,"attributes":{"foo":123.0,"bar":"wow"},"pid":"slave(1)@172.24.0.5:5051","registered_time":1518339392.10703,"resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"used_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":0.0},"offered_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":0.0},"reserved_resources":{},"unreserved_resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"active":true,"version":"1.4.0","capabilities":["MULTI_ROLE","HIERARCHICAL_ROLE","RESERVATION_REFINEMENT"],"reserved_resources_full":{},"unreserved_resources_full":[{"name":"cpus","type":"SCALAR","scalar":{"value":2.0},"role":"*"},{"name":"mem","type":"SCALAR","scalar":{"value":999.0},"role":"*"},{"name":"disk","type":"SCALAR","scalar":{"value":69716.0},"role":"*"},{"name":"ports","type":"RANGES","ranges":{"range":[{"begin":31000,"end":32000}]},"role":"*"}],"used_resources_full":[],"offered_resources_full":[]}')

    slave = mesosslave.MesosSlave(mesos_master_response)
    assert slave.is_available()

    mesos_master_response = json.loads('{"id":"40237088-f509-46a4-a5f1-c8f88ca8e03f-S0","hostname":"mesos-slave","port":5051,"attributes":{"foo":123.0,"bar":"wow"},"pid":"slave(1)@172.24.0.5:5051","registered_time":1518339392.10703,"resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"used_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":2.0},"offered_resources":{"disk":0.0,"mem":0.0,"gpus":0.0,"cpus":0.0},"reserved_resources":{},"unreserved_resources":{"disk":69716.0,"mem":999.0,"gpus":0.0,"cpus":2.0,"ports":"[31000-32000]"},"active":true,"version":"1.4.0","capabilities":["MULTI_ROLE","HIERARCHICAL_ROLE","RESERVATION_REFINEMENT"],"reserved_resources_full":{},"unreserved_resources_full":[{"name":"cpus","type":"SCALAR","scalar":{"value":2.0},"role":"*"},{"name":"mem","type":"SCALAR","scalar":{"value":999.0},"role":"*"},{"name":"disk","type":"SCALAR","scalar":{"value":69716.0},"role":"*"},{"name":"ports","type":"RANGES","ranges":{"range":[{"begin":31000,"end":32000}]},"role":"*"}],"used_resources_full":[],"offered_resources_full":[]}')

    slave = mesosslave.MesosSlave(mesos_master_response)
    assert not slave.is_available()
