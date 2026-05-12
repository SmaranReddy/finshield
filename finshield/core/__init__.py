"""
FinShield Core Module
======================

Contains core configuration, logging, and base classes.
"""

from finshield.core.config import settings
from finshield.core.logging import get_logger

__all__ = ["settings", "get_logger"]
