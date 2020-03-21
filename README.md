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

### Configuration

Environment settings are located in `.env` file. To configure current environment copy example file and fill it:
```bash
$ cp .env.example .env
```

All settings are located in `core/settings` splitted by environment. To get all settings you can simply dump it using `grep`:
```bash
$ grep -rn DJANGO_ core/settings
```

### Production

$ DJANGO_ENV=prod ./djangoctl runserver localhost:5000
