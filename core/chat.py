"""
chat.py

Coordinates conversations between the user, memory,
and the language model.
"""

from llm.base import BaseLLM
from memory.sqlite_memory import SQLiteMemory


class ChatManager:
    """
    Handles conversations between the user and Veridion.
    """

    def __init__(
        self,
        llm: BaseLLM,
        memory: SQLiteMemory,
    ) -> None:
        """
        Initialise the chat manager.

        Args:
            llm:
                Language model provider.

            memory:
                Conversation memory service.
        """

        self.llm = llm
        self.memory = memory

    def chat(self, messages: list[dict[str, str]]) -> str:
        """
        Send a conversation to the language model.

        Args:
            messages:
                Chat messages in OpenAI format.

        Returns:
            Assistant response.
        """

        response = self.llm.chat(messages)

        return response