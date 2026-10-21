.PHONY: help install install-dev install-vllm up down logs dev test lint format clean

help:  ## Show targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

install:  ## Install runtime deps
	pip install -r requirements.txt

install-dev:  ## Install dev deps
	pip install -r requirements-dev.txt

install-vllm:  ## Install vLLM on host (only needed outside Docker)
	pip install -r requirements-vllm.txt

up:  ## Start all services
	@test -f .env || (echo "Missing .env — run: cp .env.example .env" && exit 1)
	docker compose up -d --build
	@echo "Gateway: http://localhost:8000/docs"
	@echo "UI:      http://localhost:8501"

down:  ## Stop all services
	docker compose down

logs:  ## Follow logs
	docker compose logs -f

dev:  ## Run gateway locally (hot reload)
	uvicorn gateway.main:app --reload --host 0.0.0.0 --port 8000

test:  ## Run tests
	pytest -q

lint:  ## Lint
	ruff check gateway chemistry config scripts tests ui
	mypy gateway chemistry config

format:  ## Format
	ruff format .
	ruff check --fix .

clean:  ## Clean caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache .ruff_cache .mypy_cache