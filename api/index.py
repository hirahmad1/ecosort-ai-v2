"""Vercel serverless entry point — re-exports the FastAPI app."""
from backend.main import app

# Vercel Python runtime uses this as the ASGI handler
handler = app
