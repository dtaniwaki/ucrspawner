**[Prerequisites](#prerequisites)** |
**[Installation](#installation)** |
**[Configuration](#configuration)** |
**[Contributing](#contributing)** |
**[Test](#test)** |
**[License](#license)** |


# UCRSpawner

[![PyPI][pypi-image]][pypi-link]
[![PyVersions][pyversions-image]][pypi-link]
[![Build Status][build-image]][build-link]

The [JupyterHub](http://jupyterhub.readthedocs.io/en/latest/) spawner which utilizes [Universal Containerizer Runtime (UCR)](http://mesos.apache.org/documentation/latest/container-image/) in [Marathon](https://docs.mesosphere.com/1.9/deploying-services/containerizers/ucr/) so that you can use GPU.

The original idea of the Marathon integration is taken from https://github.com/vigsterkr/marathonspawner which uses Docker containerizer in Marathon.

## Prerequisites

JupyterHub 0.7 or above is required, which also means Python 3.3 or above.

## Installation

Install ucrspawner to the system:

```bash
pip install ucrspawner
```

## Configuration

Tell JupyterHub to use `UCRSpawner` by adding the following line to your `jupyterhub_config.py`:


```python
c.JupyterHub.spawner_class = 'ucrspawner.UCRSpawner'
```

### Docker Image

You can use any Docker image of [Jupyter docker stack](https://github.com/jupyter/docker-stacks) with `UCRSpawner`.

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
[pyversions-image]: https://img.shields.io/pypi/pyversions/ucrspawner.svg
[build-image]: https://travis-ci.org/dtaniwaki/ucrspawner.svg
[build-link]:  https://travis-ci.org/dtaniwaki/ucrspawner
