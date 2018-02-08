import os

c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_port = int(os.environ.get('JUPYTERHUB_API_PORT', 8080))
c.JupyterHub.hub_connect_ip = os.environ['JUPYTERHUB_API_IP']

c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

c.JupyterHub.spawner_class = 'ucrspawner.UCRSpawner'

c.Spawner.start_timeout = 3600

c.UCRSpawner.app_image = os.environ['NOTEBOOK_IMAGE']
c.UCRSpawner.app_prefix = 'jupyter'
c.UCRSpawner.marathon_host = os.environ.get('MARATHON_HOST', None)
c.UCRSpawner.cpu = 1
c.UCRSpawner.max_cpu = 4
c.UCRSpawner.mem = 256
c.UCRSpawner.max_mem = 1024
c.UCRSpawner.disk = 1000
c.UCRSpawner.max_disk = 5000
c.UCRSpawner.gpu = 0
c.UCRSpawner.max_gpu = 0
c.UCRSpawner.autotimeout = 1800
c.UCRSpawner.mesos_user = os.environ['MESOS_USER']
c.UCRSpawner.debug = True
