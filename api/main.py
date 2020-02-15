import os
import logging
import connexion

from __init__ import setup_logging
# from . import setup_logging

LOG = logging.getLogger("api")
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)


def create_app():
    app = connexion.App(
        __name__, specification_dir='.',
        options={"swagger_ui": True})
    app.add_api('api.yaml')

    setup_logging(app)

    @app.route('/healthz', methods=['GET'])
    def healthz():
        """ Health check return 200 """
        return "OK"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=5000,
        use_reloader=os.environ.get('DEBUG', False),
        debug=os.environ.get('DEBUG', False))
