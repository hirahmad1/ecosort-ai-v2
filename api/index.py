"""Vercel serverless entry-point – wraps the FastAPI app."""

from backend.main import app

handler = app
