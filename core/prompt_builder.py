"""
prompt_builder.py

Builds prompts for Veridion's language model.
"""

from __future__ import annotations

from core.prompts import SYSTEM_PROMPT
from memory.conversation import ChatMessage


class PromptBuilder:
    """
    Builds conversations for the language model.
    """

    def build(
        self,
        history: list[ChatMessage],
    ) -> list[dict[str, str]]:
        """
        Construct an OpenAI-compatible conversation.

        Args:
            history:
                Previous conversation.

        Returns:
            List of chat messages.
        """

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        for message in history:

            messages.append(
                {
                    "role": message.role,
                    "content": message.content,
                }
            )

        return messages