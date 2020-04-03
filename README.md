# Django template

Simple, but powerful starter django template for modern apps.

## Why?

* Built-in `django-admin startproject` is far from [Phoenix framework generator](https://hexdocs.pm/phoenix/up_and_running.html), no tooling, plain structure, no assets management, basically nothing. It's outdated for modern apps.
* There are many generators for django already available using [cookiecutter](https://github.com/cookiecutter/cookiecutter#python-django). But I found them too complex for starting point of my projects, even with a word `simple` in their names.

Every django project starts with copy&paste from previous project, so I decided to put basic parts here:
* managing python and html/css/js dependencies
* configuration
* deployment

## Structure

Project has monolith structure, in other words HTML pages serves from backend using django template system. I don't want to go full SPA form the start of project, it's easier to add react/angular mini-apps for dynamic parts inside django apps. Also I don't want to add REST framework form the start. Of course, in some cases it needs from the start, but in most cases no.

Django apps are located in `app/components`. I really don't like using word `apps`, because `components` are better.
Settings are splitted by enrironment in `app/settings`.
Static and other files are moved to `assets` folder, which also is used to manage javascript and css dependencies using `npm`. In case of SPA frontend you may put project there and add webpack build and use it with [django-webpack-loader](https://github.com/owais/django-webpack-loader).

Also I renamed `manage.py` to `djangoctl`, for better scripting and hisroty search.

## Development

* Development settings are 0 configuration, no need to edit anything.
* Regular django actions are available using `Makefile`, autocomplete with any shell.
* Additional tooling installed, such as `django-extensions`, `debug-toolbar` and etc.

### Editor

#### VS Code

Install `ms-python.python` and `batisteo.vscode-django` extensions.

`dev` section of `Pipfile` consists of linter, which can be enabled in vscode `settings.json` like:
```
"python.linting.lintOnSave": true,
"python.linting.flake8Enabled": true,
"python.linting.flake8Path": "flake8",
"python.linting.pylintEnabled": true,
"python.linting.pylintPath": "pylint",
"python.linting.prospectorEnabled": true,
"python.linting.prospectorPath": "prospector",
"python.formatting.provider": "autopep8",
"python.formatting.autopep8Path": "autopep8",
```

Also you might want to execute autoformat on save, so add this setting project-wide in `.vscode/settings.json` like:
```
"editor.formatOnSave": true,
```

### Install build requirements

```bash
$ brew install python postgresql memcached pyenv pipenv node
```

### Setup python

There are several ways:
1. Use package manager, already installed
2. `pyenv` can be used for setting local python version. Check how to enable it [here](https://github.com/pyenv/pyenv#installation).

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

Note:
`pipenv` can create virtual env in project by defining `PIPENV_VENV_IN_PROJECT` or see [issue comment](https://github.com/pypa/pipenv/issues/2197#issuecomment-446601760).

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

All settings are located in `app/settings` splitted by environment. To get all settings you can simply dump it using `grep`:
```bash
$ grep -rn DJANGO_ app/settings
```

To run use:
```bash
$ DJANGO_ENV=prod ./djangoctl runserver localhost:5000
```
