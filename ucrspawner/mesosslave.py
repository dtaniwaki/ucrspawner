import re

from .exceptions import UCRSpawnerException


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

    def is_available(self):
        return self.used_cpus < self.cpus and \
            self.used_mem < self.mem and \
            self.used_disk < self.disk and \
            (self.gpus == 0 or self.used_gpus < self.gpus)

    def match(self, constraint):
        if constraint.operator not in ('LIKE', 'UNLIKE'):
            raise UCRSpawnerException('Unsupported constraint operator: %s' % constraint.operator)

        if constraint.field == 'hostname':
            value = self.hostname
        else:
            value = str(self.attributes.get(constraint.field, ''))

        m = re.compile(constraint.value).match(value)
        if constraint.operator == 'LIKE':
            return m is not None
        else:
            return m is None
