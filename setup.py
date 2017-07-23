import os
import re

from setuptools import setup, find_packages


def requirements_from_file(filename='requirements.txt'):
    with open(os.path.join(os.path.dirname(__file__), filename)) as r:
        reqs = r.read().strip().split('\n')
    # Return non emtpy lines and non comments
    return [r for r in reqs if re.match(r"^\w+", r)]


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


version = '0.6.1'

README = """Python class to integrate Boto3's Cognito client so it is easy to login users. With SRP support."""

setup(
    name='warrant-ext',
    version=version,
    description=README,
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    keywords='aws,cognito,api,gateway,capless',
    author='Capless.io',
    author_email='opensource@capless.io',
    maintainer='Brian Jinwright',
    packages=find_packages(),
    package_data={
        '': ['requirements.txt']
    },
    url='https://github.com/capless/warrant',
    license='Apache License 2.0',
    install_requires=requirements_from_file(),
    extras_require={
        'test': parse_requirements('requirements_test.txt')
    },
    include_package_data=True,
    zip_safe=True,
)
