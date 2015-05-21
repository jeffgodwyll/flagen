from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from argh import ArghParser

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

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


def build():
    """
    Build site
    """
    freezer.freeze()


def serve():
    """
    Serve site
    """
    app.run()


if __name__ == '__main__':
    parser = ArghParser()
    parser.add_commands([build, serve])
    parser.dispatch()
