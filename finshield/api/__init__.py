"""
FinShield API Module
=====================

FastAPI-based REST API for the FinShield platform.
"""

from finshield.api.app import create_app
from finshield.api.routes import router

__all__ = ["create_app", "router"]
