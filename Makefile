GIT_VERSION := $(shell git describe --long --tags --always --abbrev=8 --dirty)

DOCKER_APPLICATION := backend
DOCKER_TAG ?= $(GIT_VERSION)

DOCKER_REGISTRY_REPO ?= myproject
DOCKER_IMAGE := $(DOCKER_REGISTRY_REPO)/$(DOCKER_APPLICATION)
DOCKER_BUILD_ADD_ARGS ?=

.PHONY: docker-build
docker-build:
	docker build --pull --rm --tag "$(DOCKER_IMAGE):$(DOCKER_TAG)" $(DOCKER_BUILD_ADD_ARGS) -f deployments/docker/Dockerfile .
	docker tag "$(DOCKER_IMAGE):$(DOCKER_TAG)" "$(DOCKER_IMAGE):latest"

.PHONY: docker-export
docker-export:
	docker save "$(DOCKER_IMAGE):latest" | gzip --stdout > "$(DOCKER_REGISTRY_REPO)-$(DOCKER_APPLICATION).tar.gz"

.PHONY: docker-clean
docker-clean:
	docker rmi -f "$$(docker images -q $(DOCKER_IMAGE):$(DOCKER_TAG))"

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

.PHONY: create-component
create-component:
	mkdir -pv app/components/$(name)
	$(DJANGO_MANAGE) startapp $(name) app/components/$(name)

.PHONY: admin
admin:
	$(DJANGO_MANAGE) create_superuser_with_password --username=admin --password=123qweasd --email=foo@bar.com

.PHONY: flush
flush:
	$(DJANGO_MANAGE) flush

.PHONY: info
info:
	@-python3 --version
	@-echo -n 'Django '
	@-$(DJANGO_MANAGE) version
