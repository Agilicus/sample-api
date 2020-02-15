FROM python:3.7 as builder
LABEL maintainer="don@agilicus.com"

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

FROM python:3.7
COPY api /web/api
COPY --from=builder /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin
RUN adduser --disabled-password --gecos '' api \
 && chown -R api:api /web
WORKDIR /web
USER api

ENTRYPOINT ["gunicorn", "--timeout", "10", "--keep-alive", "60", "-k", "gevent", "-b", "0.0.0.0:5000", \
            "--log-level", "info", "--access-logfile", "-", "api.main:create_app()" ]
