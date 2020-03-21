# Django template

Simple, but powerful starter django template.

## Why?

* Built-in `django-admin startproject` is far from Phoenix framework generator or RoR.
* There is many generators for django already available using [cookiecutter](https://github.com/cookiecutter/cookiecutter#python-django). But I found them too complex from the beginning for my projects.

Every django projects starts with copy&paste from previous project, so I decided to assemble basic parts here:
* installation and requirements
* configuration
* deployment
* working with modern frontend stack

## Development

* Development settings are 0 configuration, no need to edit anything.
* Regular django actions are available using `Makefile`, autocomplete with any shell.
* Additional tooling installed, such as `django-extensions`, `debug-toolbar` and etc.

### Install build requirements

```bash
$ brew install python postgresql node libmemcached memcached pyenv pipenv
```

### Setup python

1. Use package manager, already installed
2. `pyenv` can be used for setting local python version.
Check how to enable it [here](https://github.com/pyenv/pyenv#installation).

```bash
$ pyenv version

$ pyenv install
python-build: use openssl from homebrew
python-build: use readline from homebrew
Downloading Python-3.7.4.tar.xz...
```

### Install backend dependencies

Project uses [pipenv](https://pipenv.pypa.io/en/latest/basics/).

```bash
$ pipenv install
```

### Install frontend dependencies

```bash
$ cd assets
$ npm install --only=prod
```

### Launch app

To run, activate pipenv like `pipenv shell` and then execute:
```bash
$ make
$ make start
```

## Production

Environment settings are located in `.env` file. To configure current environment copy example file and fill it:
```bash
$ cp .env.example .env
```

All settings are located in `core/settings` splitted by environment. To get all settings you can simply dump it using `grep`:
```bash
$ grep -rn DJANGO_ core/settings
```

To run use:
```bash
$ DJANGO_ENV=prod ./djangoctl runserver localhost:5000
```
