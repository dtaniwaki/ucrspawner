import os
from setuptools import setup

requires = [
  'jupyterhub>=0.7',
  'marathon',
]

tests_require = [
  'pytest>=3.0,<3.3',
  'pytest-cov>=2.5,<3dev',
  'pytest-html>=1.15.2,<2dev',
]

version_ns = {}
with open(os.path.join(os.path.dirname(__file__), 'ucrspawner', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup(
    name='ucrspawner',
    version=version_ns['__version__'],
    description='JupyterHub spawner for Marathon UCR',
    url='https://github.com/dtaniwaki/ucrspawner',
    author='Daisuke Taniwaki',
    author_email='daisuketaniwaki@gmail.com',
    license='MIT',
    keywords='JupyterHub Marathon UCR Mesos',
    packages=[
        "ucrspawner",
    ],
    install_requires=requires,
    setup_requires=[
        'pytest-runner>=2.0,<3dev',
    ],
    tests_require=tests_require,
    classifiers=[
        'Framework :: Jupyter',
    ],
)
