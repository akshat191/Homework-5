from setuptools import setup, find_packages

setup(
    name = 'exercise5',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository
        'Exercise5 @ git+https://github.com/akshat191/homework5.git#egg=Exercise5-0.1'
    ]
)
