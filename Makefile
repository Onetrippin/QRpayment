DOCKER_COMPOSE = docker compose
SERVICE = app
WORKDIR = --workdir /src

CONTAINER_RUNNING_EXISTS = $(if $(shell docker ps -q --filter "name=$(SERVICE)"),true,false)

ifeq ($(CONTAINER_RUNNING_EXISTS),true)
	EXEC = $(DOCKER_COMPOSE) exec -T $(SERVICE)
else
	EXEC = $(DOCKER_COMPOSE) run --rm $(SERVICE)
endif

migrate:
	$(DOCKER_COMPOSE) run --rm $(SERVICE) python3 src/manage.py migrate $(if $m, api $m,)

makemigrations:
	$(DOCKER_COMPOSE) run --rm $(WORKDIR) $(SERVICE) python3 src/manage.py makemigrations

createsuperuser:
	$(DOCKER_COMPOSE) exec $(SERVICE) python3 src/manage.py createsuperuser

collectstatic:
	$(DOCKER_COMPOSE) run --rm $(SERVICE) python3 src/manage.py collectstatic --noinput

command:
	$(EXEC) ${c}

shell:
	$(DOCKER_COMPOSE) exec $(SERVICE) sh

debug:
	$(EXEC) debug

piplock:
	$(EXEC) pipenv install

lint:
	$(DOCKER_COMPOSE) run --rm $(WORKDIR) $(SERVICE) isort .
	$(DOCKER_COMPOSE) run --rm $(WORKDIR) $(SERVICE) flake8 --config setup.cfg
	$(DOCKER_COMPOSE) run --rm $(WORKDIR) $(SERVICE) black --config pyproject.toml .

check_lint:
	$(EXEC) isort --check --diff .
	$(EXEC) flake8 --config setup.cfg
	$(EXEC) black --check --config pyproject.toml .

build:
	$(DOCKER_COMPOSE) build

push:
	docker push ${IMAGE_APP}
	docker push ${IMAGE_BOT}

pull:
	docker pull ${IMAGE_APP}
	docker pull ${IMAGE_BOT}

up:
	$(DOCKER_COMPOSE) up --build -d

down:
	$(DOCKER_COMPOSE) down

rebuild:
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) up --build -d

clean:
	$(DOCKER_COMPOSE) down -v
	$(DOCKER_COMPOSE) rm -f
	docker rmi $$(docker images -q)

test:
	$(DOCKER_COMPOSE) run --rm $(SERVICE) pytest --disable-warnings

gen_webhook_token:
	$(EXEC) python3 -c "import secrets; print(secrets.token_urlsafe(48)[:64])"