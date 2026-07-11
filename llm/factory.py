"""
factory.py

Factory for creating language model providers.
"""

from __future__ import annotations

from config import LLM_PROVIDER

from llm.base import BaseLLM
from llm.huggingface import HuggingFaceLLM


def create_llm() -> BaseLLM:
    """
    Create and return the configured language model provider.

    Returns:
        A configured BaseLLM implementation.

    Raises:
        ValueError:
            If the configured provider is unsupported.
    """

    provider = LLM_PROVIDER.lower()

    if provider == "huggingface":
        return HuggingFaceLLM()

    raise ValueError(
        f"Unsupported LLM provider: '{LLM_PROVIDER}'"
    )