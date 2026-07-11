"""
huggingface.py

Hugging Face implementation of the Veridion language model interface.
"""

from __future__ import annotations

from huggingface_hub import InferenceClient

from config import (
    HF_TOKEN,
    MODEL_NAME,
    TEMPERATURE,
    MAX_NEW_TOKENS,
)

from llm.base import BaseLLM


class HuggingFaceLLM(BaseLLM):
    """
    Hugging Face implementation of BaseLLM.
    """

    def __init__(self) -> None:
        """
        Initialise the Hugging Face inference client.
        """

        if not HF_TOKEN:
            raise RuntimeError(
                "HF_TOKEN was not found. "
                "Please configure it in your .env file."
            )

        self.client = InferenceClient(
            token=HF_TOKEN,
        )

    def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        """
        Send a conversation to Hugging Face.

        Args:
            messages:
                OpenAI-style chat messages.

        Returns:
            Assistant response.
        """

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_NEW_TOKENS,
        )

        return response.choices[0].message.content