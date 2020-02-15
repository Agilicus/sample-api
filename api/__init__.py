import os
import logging
import json_logging


def init_logging():

    logging.basicConfig()
    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init(framework_name='connexion')

    if "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
        logging.getLogger('gunicorn.access').handlers = []

    if "hypercorn" in os.environ.get("SERVER_SOFTWARE", ""):
        logging.getLogger('hypercorn.access').handlers = []


def setup_logging(app):

    """
    Skip /healthz and /metrics records from log (either plain
    text or structured)
    """
    class HealthCheckFilter(logging.Filter):
        def filter(self, record):

            if "healthz" in record.getMessage():
                return False

            if 'request_info' in record.__dict__:
                req = record.__dict__['request_info'].request
                return "healthz" not in req.path
            return True

    class MetricsFilter(logging.Filter):
        def filter(self, record):

            if "metrics" in record.getMessage():
                return False

            if 'request_info' in record.__dict__:
                req = record.__dict__['request_info'].request
                return "metrics" not in req.path
            return True

    json_logging.init_request_instrument(app)

    hdlr = logging.getLogger('connexion-request-logger')
    hdlr.propagate = False

    for h in hdlr.handlers:
        h.addFilter(HealthCheckFilter())
        h.addFilter(MetricsFilter())


init_logging()
