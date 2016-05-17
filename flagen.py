import click

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from jinja2 import ChoiceLoader, FileSystemLoader

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_DESTINATION = 'build'
FREEZER_REMOVE_EXTRA_FILES = False
TEMPLATE_DIR = 'templates/simple'
STATIC_DIR = 'static'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('index.html', pages=pages)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template(('page.html'), page=page)


@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


def custom_template(a):
    custom_loader = ChoiceLoader([FileSystemLoader(a)])
    app.jinja_loader = custom_loader


@click.group()
def cli():
    """
    Flagen is a simple static site generator built on top of Frozen Flask
    """
    pass


@cli.command()
@click.option('--template', default=TEMPLATE_DIR,
              type=click.Path(exists=True, resolve_path=True),
              help='Pass a custom template directory')
@click.option('--static', default=STATIC_DIR, type=click.Path(exists=True),
              help='Pass a custom static directory location')
@click.option('--destination', type=click.Path(),
              help='Provide a custom destination for built files to reside in')
@click.option('--clean', is_flag=True, help='Perform clean build')
def build(template, static, clean, destination=None):
    """
    Build site and generate `build` folder
    """
    click.echo('Building site...')
    if destination:
        click.echo('Site is being stored in "{}"...'.format(destination))
        app.config.update(FREEZER_DESTINATION=destination)
    if clean:
        click.echo('Performing a clean build, ie. building from scratch...')
        app.config.update(FREEZER_REMOVE_EXTRA_FILES=True)

    custom_template(template)
    freezer.freeze()
    click.echo('Done!')


@cli.command()
@click.option('--template', default=TEMPLATE_DIR, type=click.Path(exists=True),
              help="Pass a custom template directory")
@click.option('--static', default=STATIC_DIR, type=click.Path(exists=True),
              help='Pass a custom static directory location')
def serve(template, static):
    """
    Serve site
    """
    custom_template(template)
    app.run()
