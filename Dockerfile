FROM python:3.7-slim
LABEL maintainer="don@agilicus.com"
ADD requirements.txt /tmp/requirements.txt
COPY api /web/api
RUN pip install -r /tmp/requirements.txt \
 && adduser --disabled-password --gecos '' api \
 && chown -R api:api /web
WORKDIR /web
USER api

ENTRYPOINT ["gunicorn", "--timeout", "10", "--keep-alive", "60", "-k", "gevent", "-b", "0.0.0.0:5000", \
            "--log-level", "info", "--access-logfile", "-", "api.main:create_app()" ]
