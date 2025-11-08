
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
		export DB_PORT=3306
		export DB_EXTERNAL_PORT=3307
			#
			# Can be used to access the db on the local system 
			# that already runs its own MySQL server.
	
    export DB_HOST=db
endif

COMPOSE = \
	@DB_NAME=$(DB_NAME) \
	DB_USER=$(DB_USER) \
	DB_PASSWORD=$(DB_PASSWORD) \
	DB_PORT=$(DB_PORT) \
	DB_EXTERNAL_PORT=$(DB_EXTERNAL_PORT) \
	DB_HOST=$(DB_HOST) \
	docker-compose -f $(COMPOSE_FILE)

# ------------------------------------------------
# ------------------------------------------------

.PHONY: build
build: ## Builds services
	@echo "Building services in $(APP_MODE) mode..."
	$(COMPOSE) build

.PHONY: run
run: ## Starts db and app services
	@echo "Starting services in $(APP_MODE) mode..."
	$(COMPOSE) up 
	# #
	# $(COMPOSE) up --force-recreate

.PHONY: stop
stop: ## Stops services
	@echo "Stopping services..."
	@docker-compose -f $(COMPOSE_FILE) down

.PHONY: clean-up
clean-up: ## Cleans up Docker containers and volumes
# 
# Stops and removes all containers, networks, and volumes.
#
	@echo "Cleaning up..."
	$(COMPOSE) down -v

.PHONY: restart
restart: stop run   ## Restart the stack

.PHONY: db-logs
db-logs: 
	@echo "Getting logs for db"
	$(COMPOSE) logs db

# #
.PHONY: build-and-run
build-and-run:
	@echo ""
	$(COMPOSE) up --build
