**[Prerequisites](#prerequisites)** |
**[Installation](#installation)** |
**[Configuration](#configuration)** |
**[Contributing](#contributing)** |
**[Test](#test)** |
**[License](#license)** |


# UCRSpawner

[![Build Status][build-image]][build-link]

The JupyterHub spawner which utilizes Universal Containerizer Runtime (UCR) in Marathon so that you can use GPU.

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


[build-image]: https://travis-ci.org/dtaniwaki/ucrspawner.svg
[build-link]:  https://travis-ci.org/dtaniwaki/ucrspawner
