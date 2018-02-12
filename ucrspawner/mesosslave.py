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

        self.available_cpus = params['unreserved_resources']['cpus']
        self.available_mem = params['unreserved_resources']['mem']
        self.available_disk = params['unreserved_resources']['disk']
        self.available_gpus = int(params['unreserved_resources']['gpus'])

    def is_available(self):
        return self.available_cpus > 0 and \
            self.available_mem > 0 and \
            self.available_disk > 0 and \
            (self.gpus == 0 or self.available_gpus > 0)

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
