
# PREREQUISITES

# Ensure Docker and Docker Compose are installed on your system.


# -------------------------------------------------
# Variables – can be overridden on the command line
# -------------------------------------------------

APP_MODE ?= dev
export APP_MODE

COMPOSE_FILE ?= docker-compose.yml

# Conditionally set environment variables based on APP_MODE
ifeq ($(APP_MODE), dev)
    export DB_NAME=inventory_db
    export DB_USER=user1
    export DB_PASSWORD=secretPwd
    export DB_PORT=3307
    export DB_HOST=localhost
endif

# ------------------------------------------------
# ------------------------------------------------

.PHONY: run
run: ## Starts db and app services
	@echo "Starting services in $(APP_MODE) mode..."
	@DB_NAME=$(DB_NAME) \
	DB_USER=$(DB_USER) \
	DB_PASSWORD=$(DB_PASSWORD) \
	DB_PORT=$(DB_PORT) \
	DB_HOST=$(DB_HOST) \
	docker-compose -f $(COMPOSE_FILE) up

.PHONY: stop
stop: ## Stops services
	@echo "Stopping services..."
	@docker-compose -f $(COMPOSE_FILE) down -v

.PHONY: clean-up
clean-up: ## Cleans up Docker containers and volumes
# 
# Stops and removes all containers, networks, and volumes.
# Useful for a fresh start.
#
	@echo "Cleaning up..."
	@docker-compose -f $(COMPOSE_FILE) down -v

.PHONY: re-run
restart: stop run   ## Restart the stack
