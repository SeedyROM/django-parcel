import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-parcel',
    version='0.0.1',
    packages=['parcel'],
    description='Combining Django 2.0 and Parcel in a more sane and stable way.',
    long_description=README,
    author='Zack Kollar (SeedyROM)',
    author_email='me@seedyrom.io',
    url='https://github.com/SeedyROM/django-parcel/',
    license='MIT',
    install_requires=[
        'Django>=2.0',
    ]
)