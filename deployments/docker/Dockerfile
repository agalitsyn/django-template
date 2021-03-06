FROM node:15 as frontend_build

COPY assets /build/assets
WORKDIR /build/assets

RUN npm install --only=prod


FROM python:3.9

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    gettext \
    libpq-dev && \
    apt-get clean && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN mkdir /opt/django
WORKDIR /opt/django

COPY pyproject.toml poetry.lock manage.py deployments/docker/docker-entrypoint.sh ./
COPY app ./app
COPY assets ./assets
COPY --from=frontend_build /build/assets/node_modules ./assets/node_modules

RUN $HOME/.poetry/bin/poetry config virtualenvs.create false && $HOME/.poetry/bin/poetry install --no-root --no-dev --no-interaction --no-ansi

CMD ["bash", "docker-entrypoint.sh"]
