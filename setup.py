#!/usr/bin/python3

import setuptools


requirements = []
with open('requirements.txt') as fp:
    for line in fp:
        dependency = line.strip()
        if dependency.startswith('#'):
            continue
        requirements.append(dependency)

with open('VERSION') as fp:
    version = fp.read().strip()


setuptools.setup(
    name='fileset3',
    version=version,
    description='A modern static file server.',
    license='MIT',
    author='Grow SDK Authors',
    author_email='code@grow.io',
    include_package_data=True,
    install_requires=requirements,
    package_data={
        'fileset3': [
            'cron.yaml',
            'index.yaml',
        ],
    },
    packages=setuptools.find_packages(),
    scripts=[
        'bin/fileset3',
    ],
)
