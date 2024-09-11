.PHONY:install
install:
	poetry install

.PHONY:django-shell
django-shell:
	poetry run python -m core.manage shell

.PHONY:dbshell
dbshell:
	poetry run python -m core.manage dbshell

.PHONY:migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY:show-migrations
show-migrations:
	poetry run python -m core.manage showmigrations --plan

.PHONY:migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY:sever
server:
	poetry run python -m core.manage runserver

.PHONY:admin
admin:
	poetry run python -m core.manage create_default_admin

.PHONY:lint
lint:
	git add .; poetry run pre-commit run --all-files

.PHONY:update-precommit
update-precommit:
	poetry run pre-commit uninstall; poetry run pre-commit clean; poetry run pre-commit install

.PHONY:test
test:
	@RUNNING_MODE=test \
	poetry run pytest $(ARGS)

.PHONY:test-lf
test-lf:
	@RUNNING_MODE=test \
	poetry run pytest -v -rs --lf

.PHONY:test-r
test-r:
	@RUNNING_MODE=test \
	poetry run pytest -v -rs -n auto --show-capture=no --cache-clear \
	--cov=core --cov-report term-missing --cov-report html --cov-config=pyproject.toml

.PHONY:test-d
test-d:
	docker-compose exec app make test-r

.PHONY:up-dependencies-only
up-dependencies-only:
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY:local-project-up
local-project-up:
	docker-compose -f local.yml up --build -d --remove-orphans

.PHONY:local-project-down
local-project-down:
	docker-compose -f local.yml down

.PHONY:local-db-backup
local-db-backup:
	docker-compose -f local.yml exec postgres backup

.PHONY:local-backup-list
local-backup-list:
	docker-compose -f local.yml exec postgres backups

.PHONY:local-db-restore
local-db-restore:
	docker-compose -f local.yml exec postgres restore $(F)

.PHONY:docker-logs
docker-logs:
	docker-compose -f local.yml logs

.PHONY:commit
commit:
	poetry run cz commit

.PHONY:bump
bump:
	poetry run cz bump

.PHONY:update
update: install migrate update-precommit ;

.PHONY:load-fixtures
load-fixtures:
	poetry run python -m core.manage load_fixtures

.PHONY:extract-db
extract-db:
	poetry run python -m core.manage dumpdata > core/product/fixtures/fixtures.json

.PHONY:dump-models
dump-models:
	poetry run python -m core.manage dump_models
