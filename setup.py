import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.rst')) as f:
    readme = f.read()


with open('requirements.txt') as r:
    req = r.read().splitlines()


setup(
    name='flagen',
    version='0.1',
    url='https://github.com/jeffgodwyll/flagen',
    author_email='hi@jeffgodwyll.com',
    description='A flask static site generator that uses markdown and jinja2 '
    'templates.',
    long_description=readme,
    py_modules=['flagen'],
    install_requires=req,
    entry_points='''
        [console_scripts]
        flagen=flagen:cli
    ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
