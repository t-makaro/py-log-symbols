from setuptools import setup, find_packages # pylint: disable=no-name-in-module,import-error

def readme():
    with open('README.md') as f:
        return f.read()

def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()

setup(
    name='log_symbols',
    packages=find_packages(exclude=('tests',)),
    version='0.0.4',
    description='Colored symbols for various log levels for Python',
    long_description=readme(),
    author='Manraj Singh',
    author_email='manrajsinghgrover@gmail.com',
    url='https://github.com/ManrajGrover/py-log-symbols',
    keywords=[
        'log symbols',
        'symbols',
        'log'
    ],
    install_requires=dependencies('requirements.txt'),
    tests_require=dependencies('requirements-dev.txt')
)
