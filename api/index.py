"""Vercel serverless entry point for EcoSort AI FastAPI app."""
import os
import sys

# Ensure project root is on sys.path so `backend` package resolves
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Set defaults so lifespan doesn't crash on missing env vars
os.environ.setdefault("HF_TOKEN", os.environ.get("HF_TOKEN", "placeholder"))
os.environ.setdefault("HF_RECIPE_MODEL", "flax-community/t5-recipe-generation")
os.environ.setdefault("HF_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

from backend.main import app  # noqa: E402

# Eagerly initialize food_scanner for serverless (lifespan may not fire)
try:
    from backend.vision import FoodScanner
    import backend.main as main_mod
    if main_mod.food_scanner is None:
        token = os.environ.get("HF_TOKEN", "")
        if token and token != "placeholder":
            main_mod.food_scanner = FoodScanner(token=token)
except Exception:
    pass

# Eagerly connect MongoDB
try:
    from backend.db import get_db
    import backend.main as main_mod
    if not main_mod.mongo_ok:
        get_db()
        main_mod.mongo_ok = True
        from backend.store import UserStore
        if main_mod.store is None:
            main_mod.store = UserStore()
except Exception:
    pass

# Vercel Python runtime ASGI handler
handler = app
