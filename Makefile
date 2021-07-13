env-up:
	docker-compose up -d --build
.PHONY: env-up

env-down:
	docker-compose down
.PHONY: env-down
