"""Vercel serverless entry point for EcoSort AI FastAPI app."""
import os
import sys
import traceback

# Ensure project root is on sys.path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Set env defaults before any imports
os.environ.setdefault("HF_TOKEN", "placeholder")
os.environ.setdefault("HF_RECIPE_MODEL", "flax-community/t5-recipe-generation")
os.environ.setdefault("HF_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
os.environ.setdefault("MONGODB_DB", "ecosort_ai")

try:
    from fastapi import FastAPI
    from backend.main import app
    handler = app
except Exception:
    # Fallback: minimal error-reporting app
    app = FastAPI()

    @app.get("/api/{path:path}")
    @app.post("/api/{path:path}")
    async def error_handler(path: str):
        return {
            "error": "EcoSort backend failed to initialize",
            "traceback": traceback.format_exc(),
            "python_path": sys.path,
            "root": ROOT,
        }

    @app.get("/")
    async def root():
        return {"status": "fallback", "error": traceback.format_exc()}

    handler = app
