FROM node:14 as frontend_build

COPY assets /build/assets
WORKDIR /build/assets

RUN npm install --only=prod


FROM python:3.8

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # pipenv:
    PIPENV_VENV_IN_PROJECT=1

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    gettext \
    libpq-dev && \
    apt-get clean && \
    curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python

RUN mkdir /opt/django
WORKDIR /opt/django

COPY Pipfile Pipfile.lock manage.py deployments/docker/docker-entrypoint.sh ./
COPY app ./app
COPY assets ./assets
COPY --from=frontend_build /build/assets/node_modules ./assets/node_modules

RUN pipenv install --ignore-pipfile --system

CMD ["bash", "docker-entrypoint.sh"]
