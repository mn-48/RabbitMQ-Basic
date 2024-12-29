# Variables
PYTHON = python
MANAGE = $(PYTHON) manage.py
DOCKER_COMPOSE = docker-compose

# DOCKER_COMPOSE_RUN = sudo docker compose run web
DOCKER_COMPOSE_RUN = docker-compose run projectb

# Default target (help)
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make migrations       - Create database migrations"
	@echo "  make migrate          - Apply database migrations"
	@echo "  make collectstatic    - Collect static files"
	@echo "  make runserver        - Run the Django development server"
	@echo "  make all              - Run migrations, collect static files, and start the server"
	@echo "  make shell            - Start a Django shell"
	@echo "  make up               - Start Docker containers"
	@echo "  make build            - Build and start Docker containers"
	@echo "  make down             - Stop Docker containers"

# Targets
.PHONY: migrations
migrations:
	$(DOCKER_COMPOSE_RUN) $(MANAGE) makemigrations

.PHONY: migrate
migrate:
	$(DOCKER_COMPOSE_RUN) $(MANAGE) migrate

.PHONY: collectstatic
collectstatic:
	$(DOCKER_COMPOSE_RUN) $(MANAGE) collectstatic --noinput

.PHONY: runserver
runserver:
	$(DOCKER_COMPOSE_RUN) $(MANAGE) runserver 0.0.0.0:8000

.PHONY: createsuperuser
createsuperuser:
	$(DOCKER_COMPOSE_RUN) $(MANAGE) createsuperuser 

.PHONY: all
all: migrations migrate collectstatic runserver



.PHONY: up
up:
	$(DOCKER_COMPOSE) up

.PHONY: build
build:
	$(DOCKER_COMPOSE) up --build -d

.PHONY: logs
logs:
	$(DOCKER_COMPOSE) logs


.PHONY: sh
sh:
	$(DOCKER_COMPOSE_RUN) sh

.PHONY: shell
shell:
	$(DOCKER_COMPOSE_RUN) $(MANAGE) shell	

.PHONY: down
down:
	$(DOCKER_COMPOSE) down
