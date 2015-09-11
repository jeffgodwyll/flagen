from setuptools import setup

setup(
    name='flagen',
    version='0.1',
    url='https://github.com/jeffgodwyll/flagen',
    author_email='hi@jeffgodwyll.com',
    description='A flask static site generator that uses markdown and jinja2 '
    'templates.',
    py_modules=['flagen'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        flagen=flagen:cli
    ''',
)
