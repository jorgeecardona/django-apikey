from setuptools import setup, find_packages
from os import path
BASE_DIR = path.abspath(path.dirname(__file__))


setup(
    name='django-apikey',
    description='Simple Key authentication for Django.'\
    'Based on  github.com/scoursen/django-apikey',
    version='0.1.7',
    long_description=open(path.join(BASE_DIR, 'README.rst')).read(),
    url='https://www.github.com/jorgeecardona/django-apikey',
    packages=find_packages(),
    author='Jorge Eduardo Cardona',
    author_email='jorgeecardona@gmail.com',
    license='BSD',
    keywords='django authentication piston',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        ],
    )
