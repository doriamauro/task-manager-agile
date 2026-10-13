"""FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(
    title="TaskManager API",
    description="REST API for managing tasks.",
    version="0.1.0",
)


