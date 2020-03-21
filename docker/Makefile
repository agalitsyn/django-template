# Docker targets
GIT_VERSION := $(shell git describe --long --tags --always --abbrev=8 --dirty)

DOCKER_APPLICATION := backend
DOCKER_TAG ?= $(GIT_VERSION)

DOCKER_REGISTRY_REPO ?= app
DOCKER_IMAGE := $(DOCKER_REGISTRY_REPO)/$(DOCKER_APPLICATION)
DOCKER_BUILD_ADD_ARGS ?=

.PHONY: docker-build
docker-build:
	docker build --pull --rm --tag "$(DOCKER_IMAGE):$(DOCKER_TAG)" $(DOCKER_BUILD_ADD_ARGS) .
	docker tag "$(DOCKER_IMAGE):$(DOCKER_TAG)" "$(DOCKER_IMAGE):latest"

.PHONY: docker-export
docker-export:
	docker save "$(DOCKER_IMAGE):latest" | gzip --stdout > "$(DOCKER_REGISTRY_REPO)-$(DOCKER_APPLICATION).tar.gz"

.PHONY: docker-clean
docker-clean:
	docker rmi -f "$$(docker images -q $(DOCKER_IMAGE):$(DOCKER_TAG))"
