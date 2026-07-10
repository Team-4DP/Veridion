"""
conversation.py

Defines the data structures used to represent conversations
within Veridion.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ChatMessage:
    """
    Represents a single message in a conversation.

    Attributes:
        role:
            The sender of the message.
            Expected values are typically:
            - "system"
            - "user"
            - "assistant"

        content:
            The text content of the message.
    """

    role: str
    content: str