from setuptools import setup, find_packages

setup(
    name='django-apikey',
    description='Simple Key authentication for Django.'\
    'Based on  github.com/scoursen/django-apikey',
    version='0.1.6',
    long_description=open('README.rst').read(),
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
