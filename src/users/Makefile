# Makefile for users MCP Server

.PHONY: help install test test-unit test-integration lint format clean

# Default target
help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  test        - Run tests"
	@echo "  lint        - Run linting"
	@echo "  format      - Format code"
	@echo "  clean       - Clean build artifacts"
	@echo ""
	@echo "Note: MCP servers must be started by MCP clients (VS Code, Claude Desktop, etc.)."
	@echo "      Do not run directly from the terminal. See README.md for configuration."

# Install dependencies
install:
	@if command -v uv >/dev/null 2>&1; then \
		echo "Installing with uv..."; \
		uv sync --extra dev; \
	else \
		echo "uv not found, falling back to pip..."; \
		python3 -m pip install -e ".[dev]"; \
	fi

# Run tests
test: install
	@if command -v uv >/dev/null 2>&1; then \
		echo "Running full test suite with uv..."; \
		uv run pytest --cov=. --cov-report=term-missing; \
	else \
		echo "Running full test suite with python3..."; \
		python3 -m pytest --cov=. --cov-report=term-missing; \
	fi

test-unit: install
	@if command -v uv >/dev/null 2>&1; then \
		echo "Running unit tests with uv..."; \
		uv run pytest -m "not integration" --cov=. --cov-report=term-missing; \
	else \
		echo "Running unit tests with python3..."; \
		python3 -m pytest -m "not integration" --cov=. --cov-report=term-missing; \
	fi

test-integration: install
	@if command -v uv >/dev/null 2>&1; then \
		echo "Running integration tests with uv..."; \
		uv run pytest tests/integration -m integration -xvs; \
	else \
		echo "Running integration tests with python3..."; \
		python3 -m pytest tests/integration -m integration -xvs; \
	fi

# Run linting
lint: install
	@if command -v uv >/dev/null 2>&1; then \
		echo "Running linting with uv..."; \
		uv run ruff check .; \
		uv run mypy .; \
	else \
		echo "Running linting with python3..."; \
		python3 -m ruff check .; \
		python3 -m mypy .; \
	fi

# Format code
format: install
	@if command -v uv >/dev/null 2>&1; then \
		echo "Formatting code with uv..."; \
		uv run black .; \
		uv run isort .; \
		uv run ruff check . --fix; \
	else \
		echo "Formatting code with python3..."; \
		python3 -m black .; \
		python3 -m isort .; \
		python3 -m ruff check . --fix; \
	fi

# Clean build artifacts
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf dist/
	rm -rf bin/