# Wraps manage.py actions for predefined actions
# Only for dev purposes

ifndef VIRTUAL_ENV
$(error VIRTUAL_ENV not specified, did you forget to source virtualenv?)
endif

DJANGO_MANAGE := $$(pwd)/djangoctl

.PHONY: all
all: check static compilemessages migrate

.PHONY: lint
lint:
	flake8 .

.PHONY: check
check:
	$(DJANGO_MANAGE) check --fail-level WARNING

.PHONY: shell
shell:
	$(DJANGO_MANAGE) shell

.PHONY: dbshell
dbshell:
	$(DJANGO_MANAGE) dbshell

.PHONY: start
start: check
	$(DJANGO_MANAGE) runserver localhost:5000

.PHONY: migrate
migrate:
	$(DJANGO_MANAGE) migrate

.PHONY: migrations
migrations:
	$(DJANGO_MANAGE) makemigrations

.PHONY: showmigrations
showmigrations:
	$(DJANGO_MANAGE) showmigrations

.PHONY: static
static:
	$(DJANGO_MANAGE) collectstatic --no-input

.PHONY: messages
messages:
	$(DJANGO_MANAGE) makemessages --verbosity 3 --locale ru --ignore assets --ignore docker

.PHONY: compilemessages
compilemessages:
	$(DJANGO_MANAGE) compilemessages --verbosity 3 --locale ru

.PHONY: admin
admin:
	$(DJANGO_MANAGE) createsuperuserwithpassword --username=admin --password=123qweasd --email=foo@bar.com

.PHONY: flush
flush:
	$(DJANGO_MANAGE) flush

.PHONY: info
info:
	@-python3 --version
	@-echo -n 'Django '
	@-$(DJANGO_MANAGE) version
