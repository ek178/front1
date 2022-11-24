import flask

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.get('/')
def index():
    return flask.render_template('home/index.html')
