"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ███████╗██╗███╗   ██╗███████╗██╗  ██╗██╗███████╗██╗     ██████╗            ║
║   ██╔════╝██║████╗  ██║██╔════╝██║  ██║██║██╔════╝██║     ██╔══██╗           ║
║   █████╗  ██║██╔██╗ ██║███████╗███████║██║█████╗  ██║     ██║  ██║           ║
║   ██╔══╝  ██║██║╚██╗██║╚════██║██╔══██║██║██╔══╝  ██║     ██║  ██║           ║
║   ██║     ██║██║ ╚████║███████║██║  ██║██║███████╗███████╗██████╔╝           ║
║   ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝            ║
║                                                                               ║
║   🛡️  FinShield - Financial Crime Intelligence Platform                       ║
║   Enterprise-Grade AML Detection & Investigation System                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

FinShield is a next-generation Anti-Money Laundering (AML) detection platform
powered by advanced AI, graph-based workflows, and intelligent reasoning.

Features:
---------
• Chain-of-Thought (CoT) & ReAct reasoning for intelligent analysis
• Multi-agent LangGraph orchestration
• Real-time transaction monitoring
• Network analysis for hidden relationships
• Regulatory compliance automation (SAR/STR generation)
• Risk-based case prioritization
• Human-in-the-loop review workflows

Author: Kunal Shaw
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Kunal Shaw"
__license__ = "MIT"

from finshield.core.config import settings
from finshield.core.logging import get_logger

logger = get_logger(__name__)

# Package exports
__all__ = [
    "__version__",
    "settings",
    "logger",
]
