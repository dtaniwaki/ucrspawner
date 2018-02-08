**[Prerequisites](#prerequisites)** |
**[Installation](#installation)** |
**[Configuration](#configuration)** |
**[Contributing](#contributing)** |
**[Test](#test)** |
**[License](#license)** |


# UCRSpawner

[![PyPI][pypi-image]][pypi-link]
[![GitHub license][license-image]][license-link]
[![PyVersions][pyversions-image]][pypi-link]
[![Build Status][build-image]][build-link]
[![codecov][cov-image]][cov-link]


The [JupyterHub](http://jupyterhub.readthedocs.io/en/latest/) spawner which utilizes [Universal Containerizer Runtime (UCR)](http://mesos.apache.org/documentation/latest/container-image/) in [Marathon](https://docs.mesosphere.com/1.9/deploying-services/containerizers/ucr/) so that you can use GPU.

The original idea of the Marathon integration is taken from https://github.com/vigsterkr/marathonspawner which uses Docker containerizer in Marathon.

## Prerequisites

JupyterHub 0.7 or above is required, which also means Python 3.3 or above.

## Installation

Install ucrspawner to the system:

```sh
pip install ucrspawner
```

## Installation from GitHub

```sh
git clone https://github.com/dtaniwaki/ucrspawner
cd ucrspawner
python setup.py install
```

## Configuration

Tell JupyterHub to use `UCRSpawner` by adding the following line to your `jupyterhub_config.py`:


```python
c.JupyterHub.spawner_class = 'ucrspawner.UCRSpawner'
```

Then, specify the endpoint of Marathon.

```python
c.UCRSpawner.marathon_host = "MARATHON_ENDPOINT"
```

### App Image

Users can use any Docker image of [Jupyter docker stack](https://github.com/jupyter/docker-stacks) with `UCRSpawner`.

Set the default app image if you want to change.

```python
c.UCRSpawner.app_image = 'jupyterhub/singleuser'
```

Users can choose their own app image in the spawn option form as well.

Specify a user in Mesos slaves whose `UID` is the same as a user in your Docker image.

```python
c.UCRSpawner.mesos_user = 'jovyan_in_mesos'
```

In the default user of docker stacks `jovyan`'s `UID` is `1000`, so you must have a user whose `UID` is `1000` in Mesos slaves as well. Otherwise, you need to change the `UID` of jovyan in Docker image instead.

You can also change the app ID prefix of Marathon.

```python
c.UCRSpawner.app_prefix = 'jupyter'
```

### Resource Limits

While UCRSpawner has minimum computing resource limits, you can configure default and maximum resource limits.

```python
c.UCRSpawner.cpu = 1
c.UCRSpawner.max_cpu = 4
c.UCRSpawner.mem = 256 // in MB
c.UCRSpawner.max_mem = 1024 // in MB
c.UCRSpawner.disk = 1000 // in MB
c.UCRSpawner.max_disk = 5000 // in MB
c.UCRSpawner.gpu = 0
c.UCRSpawner.max_gpu = 2
```

### Auto timeout

You can automatically stop running notebook servers which doesn't make any communication with the hub. Set the timeout period.

```python
c.UCRSpawner.autotimeout = 1800 // in seconds
```

## Test

```sh
python setup.py test
```

Or use `tox` to test this package in multiple python versions.

```sh
tox
```

### Test UCRSpawner on JupyterHub

You can launch JupyterHub and the dependencies with UCRSpawner by docker-compose.

```sh
docker-compose --project-name=ucrspawner up
```

Wait for a while until all the services up, then, you will get access to JupyterHub at `http://localhost:8000`, Marathon at `http://localhost:8080` and Mesos Master at `http://localhost:5050`.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new [Pull Request](../../pull/new/master)

## Copyright

Copyright (c) 2018 Daisuke Taniwaki. See [LICENSE](LICENSE) for details.


[pypi-image]:  https://img.shields.io/pypi/v/ucrspawner.svg
[pypi-link]:   https://pypi.python.org/pypi/ucrspawner
[license-image]: https://img.shields.io/github/license/dtaniwaki/ucrspawner.svg
[license-link]:  https://github.com/dtaniwaki/ucrspawner
[pyversions-image]: https://img.shields.io/pypi/pyversions/ucrspawner.svg
[build-image]: https://travis-ci.org/dtaniwaki/ucrspawner.svg
[build-link]:  https://travis-ci.org/dtaniwaki/ucrspawner
[cov-image]:   https://codecov.io/gh/dtaniwaki/ucrspawner/branch/master/graph/badge.svg
[cov-link]:    https://codecov.io/gh/dtaniwaki/ucrspawner
