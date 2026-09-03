"""Vercel serverless entry point for EcoSort AI FastAPI app."""
import os
import sys

# Ensure project root is on sys.path so `backend` package resolves
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Patch lifespan to not crash on missing env vars in serverless
os.environ.setdefault("HF_TOKEN", "placeholder")

from backend.main import app  # noqa: E402

# Vercel Python runtime ASGI handler
handler = app
