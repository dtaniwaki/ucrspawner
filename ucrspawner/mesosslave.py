import re

from .exceptions import UCRSpawnerException
from .utils import remove_zeros


class MesosSlave():
    def __init__(self, params):
        self.hostname = params['hostname']
        self.attributes = params['attributes']

        self.disk = params['resources']['disk']
        self.cpus = params['resources']['cpus']
        self.mem = params['resources']['mem']
        self.disk = params['resources']['disk']
        self.gpus = int(params['resources']['gpus'])

        self.used_cpus = params['used_resources']['cpus']
        self.used_mem = params['used_resources']['mem']
        self.used_disk = params['used_resources']['disk']
        self.used_gpus = int(params['used_resources']['gpus'])

    def is_empty(self):
        return self.used_cpus == 0 and \
            self.used_mem == 0 and \
            self.used_disk == 0 and \
            self.used_gpus == 0

    def is_available(self):
        return self.used_cpus < self.cpus and \
            self.used_mem < self.mem and \
            self.used_disk < self.disk and \
            (self.gpus == 0 or self.used_gpus < self.gpus)

    def is_occupied(self):
        return self.used_cpus >= self.cpus or \
            self.used_mem >= self.mem or \
            self.used_disk >= self.disk or \
            (self.gpus != 0 and self.used_gpus >= self.gpus)

    # Match Mesos slaves with Marathon constraints
    #   https://github.com/mesosphere/marathon/blob/v1.5.1/src/main/scala/mesosphere/mesos/Constraints.scala#L34
    def match(self, constraint):
        if constraint.operator not in ('LIKE', 'UNLIKE', 'IS'):
            raise UCRSpawnerException('Unsupported constraint operator: %s' % constraint.operator)
        if not isinstance(constraint.value, str):
            raise UCRSpawnerException('Unsupported constraint value type: %s' % type(constraint.value))

        if constraint.field == 'hostname':
            value = self.hostname
        else:
            value = self.attributes.get(constraint.field, '')

        if isinstance(value, (int, float)):
            value = remove_zeros(value)
        elif isinstance(value, str):
            # Ignore range and set attributes
            if re.match('^(\\[.*\\]|\\{.*\\})$', value):
                return False
        else:
            raise UCRSpawnerException('Unsupported value type: %s' % type(value))

        m = re.match('^%s$' % constraint.value, value)
        if constraint.operator == 'LIKE':
            return m is not None
        else:
            return m is None
