FROM python:3.6-stretch

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm \
    PYTHONUNBUFFERED=1 \
    PIPENV_VENV_IN_PROJECT=1

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
        gettext \
        libpq-dev && \
    apt-get clean &&
    curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python

RUN mkdir /opt/django
WORKDIR /opt/django

COPY . .

RUN pipenv sync


CMD ["bash", "docker-entrypoint.sh"]
