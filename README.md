# Django template

Simple, but powerful starter django template.

;tldr
Backend - Nginx + Uvcorn + Django 3 LTS + PostgreSQL 12 + memcached
Frontend - Django templates + Bootstrap 4 + JQuery 3

## Why?

- Built-in `django-admin startproject` is far from [Phoenix framework generator](https://hexdocs.pm/phoenix/up_and_running.html), no tooling, plain structure, no assets management, basically nothing. It's outdated for modern apps.
- There are many generators for django already available using [cookiecutter](https://github.com/cookiecutter/cookiecutter#python-django). But I found them too complex for starting point for my projects, even with a word `simple` in their names they are not so simple.

Generally, django project starts with copy&paste from previous project, so I decided to put basic parts here:

- managing python and html/css/js dependencies
- configuration
- deployment

## Structure

Project has monolith structure, in other words HTML pages serves from backend using django template system. I don't want to go full SPA form the start of project, it's easier to add react/angular mini-apps for dynamic parts inside django apps. Also I don't want to add REST framework form the start. Of course, in some cases it needs from the start, but in most cases no.

Django apps are located in `app/components`. I really don't like using word `apps`, because `components` are better.
Settings are splitted by enrironment in `app/settings`.
Static and other files are moved to `assets` folder, which also is used to manage javascript and css dependencies using `npm`. In case of SPA frontend you may put project there and add webpack build and use it with [django-webpack-loader](https://github.com/owais/django-webpack-loader).

## Development

- Development settings are 0 configuration, no need to edit anything.
- Regular django actions are available using `Makefile`, autocomplete with any shell.
- Additional tooling installed, such as `django-extensions`, `debug-toolbar` and etc.

### Editor

Repository consists of pre-configured settings for VS Code and Pycharm, see `.vscode` and `.idea` folders.

#### VS Code

Install `ms-python.python` and `batisteo.vscode-django` extensions.

dev dependencies has linter, which can be enabled in vscode `settings.json` like:

```
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "python.languageServer": "Microsoft",
  "python.linting.lintOnSave": true,
  "python.linting.prospectorEnabled": true,
  "python.linting.prospectorPath": "prospector",
  "python.linting.prospectorArgs": ["--max-line-length", "120", "--ignore-paths", ".venv"],
  "python.formatting.provider": "black",
  "python.formatting.blackPath": "black",
  "python.formatting.blackArgs": ["--line-length", "120"],
}
```

Also you might want to execute autoformat on save and enabling virtualenv, so add this setting project-wide in `.vscode/settings.json` like:

```
{
    "editor.formatOnSave": true,
    "python.pythonPath": "${workspaceFolder}/.venv/bin/python"
}
```

#### Pycharm

To achieve same functionality on auto-formatting you need to install `File Watchers` plugin.

Configs are already exists in this repository, for manual installation follow links:

- [Setup black](https://black.readthedocs.io/en/stable/editor_integration.html#pycharm-intellij-idea)
- [Setup prettier](https://prettier.io/docs/en/webstorm.html#running-prettier-on-save-using-file-watcher)

### Install build requirements

```bash
$ brew install python pyenv poetry node
```

### Install libraries for python modules

```bash
$ brew install postgresql memcached
```

### Setup python

There are several ways:

1. Using package manager, should be already installed
2. `pyenv` can be used for setting local python version. Check how to enable it [here](https://github.com/pyenv/pyenv#installation).

```bash
$ pyenv version

$ pyenv install
python-build: use openssl from homebrew
python-build: use readline from homebrew
Downloading Python-3.9.tar.xz...
```

### Install backend dependencies

Project uses [poetry](https://python-poetry.org/docs/#installation).

```bash
$ poetry install
```

### Install frontend dependencies

```bash
$ cd assets
$ npm install
```

### Launch app

To run, activate pipenv like `poetry shell` and then execute:

```bash
$ make
$ make start
```

## Production configuration

Environment settings are located in `.env` file. To configure current environment copy example file and fill it:

```bash
$ cp .env.example .env
```

All settings are located in `app/settings` splitted by environment. To get all settings you can simply dump it using `grep`:

```bash
$ grep -rn DJANGO_ app/settings
```

To run use:

```bash
$ DJANGO_ENV=prod ./manage.py runserver localhost:5000
```

## Deployment

### Docker

For many MVPs docker is easy to go strategy for the first deployments. Also docker provides pre-configured dev environment,
which is very close to actual production (non-docker) deployments in terms of separated infrastructure components, like nginx proxy.

#### Prerequisites

- [docker-ce](https://docs.docker.com/engine/installation)
- [docker-compose](https://docs.docker.com/compose)

#### Build

```bash
$ make docker-build
```

Building docker images is separated from docker-compose, because I prefer to user docker-compose only as container launcher,
not as all-in-one solution. When project goes we can switch to container schedulers like docker swarm or kubernetes,
but build process will stay unchanged.

#### Run

```bash
$ cd deployments/docker
$ docker-compose up
```

Open http://localhost:8080
