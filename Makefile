
# PREREQUISITES

# Ensure Docker and Docker Compose are installed on your system.


# -------------------------------------------------
# Variables – can be overridden on the command line
# -------------------------------------------------

APP_MODE ?= dev          # default mode
export APP_MODE

COMPOSE_FILE ?= docker-compose.yml

# Conditionally set environment variables based on APP_MODE
ifeq ($(APP_MODE), dev)
    export DB_HOST=localhost
    export DB_PORT=3307
    export DB_USER=root
    export DB_PASSWORD=secretRootPwd
    export DB_NAME=inventory_db
else
    export DB_HOST=prod_db
    export DB_PORT=3306
    export DB_USER=prod_user
    export DB_PASSWORD=prod_password
    export DB_NAME=prod_database
endif
# -------------------------------------------------
# -------------------------------------------------


.PHONY: run
run: ## Starts db and app services
	@echo "Starting services in $(APP_MODE) mode..."
  @docker-compose -f $(COMPOSE_FILE) up

.PHONY: stop
stop ## Stops services
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
