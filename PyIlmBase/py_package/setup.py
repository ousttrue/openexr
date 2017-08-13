#!/usr/bin/env python

from setuptools import setup, Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


setup(
        name='alembic',
        version='0.1',
        description='Alembic Library',
        packages=['ilm', 'iex', 'imath', 'alembic', 'alembicgl'],
        package_data={
            'ilm':['*.pyd', '*.dll'],
            },
        distclass=BinaryDistribution
        )

