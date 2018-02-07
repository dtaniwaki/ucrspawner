import os

from setuptools import setup

requires = [
    'jupyterhub>=0.7,<1dev',
    'marathon>=0.9,<1dev',
]

tests_require = [
    'pytest>=3.0,<3.3',
    'pytest-cov>=2.5,<3dev',
    'pytest-html>=1.15.2,<2dev',
    'codecov>=1.4.0,<2dev',
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
    python_requires='>=3.3',
    install_requires=requires,
    setup_requires=[
        'pytest-runner>=2.0,<3dev',
        'tox>=2.7,<3dev',
        'bumpversion>=0.5.3,<1dev',
    ],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'flake8': [
            'flake8>=3.5.0,<4dev',
            'autoflake>=1.1,<2dev',
            'autopep8>=1.3,<2dev',
            'flake8-blind-except>=0.1.1,<1dev',
            'flake8-import-order>=0.16,<1dev',
            'flake8-html>=0.4.0,<1dev',
        ],
        'cov': [
            'coverage>=4.5.0,<5dev',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Jupyter',
    ],
)
