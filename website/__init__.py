import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from . import webpage
    app.register_blueprint(webpage.bp)
    app.add_url_rule('/', endpoint='webpage.render')
    app.add_url_rule('/webpage', endpoint='webpage.render')
    app.add_url_rule('/webpage/render', endpoint='webpage.render')

    return app