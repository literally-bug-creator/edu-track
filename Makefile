build:
	@docker compose build


build-dev:
	@docker compose -f docker-compose.dev.yaml build


run:
	@docker compose up -d


run-dev:
	@docker compose -f docker-compose.dev.yaml up -d


stop:
	@docker compose stop


down:
	@docker compose down

down-dev:
	@docker compose -f docker-compose.dev.yaml down


restart:
	@docker compose restart


%:
	@:
