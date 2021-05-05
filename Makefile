# Wraps manage.py actions for predefined actions
# Only for dev purposes
# TODO: do not do this check for docker targets
ifndef VIRTUAL_ENV
$(error VIRTUAL_ENV not specified, did you forget to source virtualenv?)
endif

DJANGO_MANAGE := $$(pwd)/manage.py

.PHONY: all
all: check static compilemessages migrate

.PHONY: lint
lint:
	prospector --max-line-length 120 --ignore-paths .venv

.PHONY: check
check:
	$(DJANGO_MANAGE) check --fail-level WARNING

.PHONY: shell
shell:
	$(DJANGO_MANAGE) shell_plus

.PHONY: dbshell
dbshell:
	$(DJANGO_MANAGE) dbshell

.PHONY: start
start: check
	$(DJANGO_MANAGE) runserver_plus localhost:8080

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
	$(DJANGO_MANAGE) makemessages --verbosity 3 --locale ru --ignore assets --ignore deployments --ignore .venv --ignore html

.PHONY: compilemessages
compilemessages:
	$(DJANGO_MANAGE) compilemessages --verbosity 3 --locale ru

.PHONY: create-component
create-component:
	mkdir -pv app/components/$(name)
	$(DJANGO_MANAGE) startapp $(name) app/components/$(name)

.PHONY: create-component-command
create-component-command:
	$(DJANGO_MANAGE) create_command $(name)

.PHONY: create-component-tags
create-component-tags:
	mkdir -pv app/components/$(name)
	$(DJANGO_MANAGE) create_template_tags $(name)

.PHONY: admin
admin:
	$(DJANGO_MANAGE) create_superuser_with_password --username=admin --password=123qweasd --email=foo@bar.com
	$(DJANGO_MANAGE) set_default_site --name localhost --domain localhost:8080

.PHONY: reset-schema
reset-schema:
	$(DJANGO_MANAGE) reset_schema

.PHONY: info
info:
	@-python3 --version
	@-echo -n 'Django '
	@-$(DJANGO_MANAGE) version

include docker.mk
