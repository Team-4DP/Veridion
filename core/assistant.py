"""
assistant.py

Main Veridion assistant class.
"""

from config import DATABASE_PATH

from core.prompts import SYSTEM_PROMPT
from core.chat import ChatManager

from llm.factory import create_llm

from memory.sqlite_memory import SQLiteMemory


class Veridion:
    """
    Main Veridion assistant.
    """

    def __init__(self) -> None:

        self.memory = SQLiteMemory(DATABASE_PATH)

        self.llm = create_llm()

        self.chat_manager = ChatManager(
            llm=self.llm,
            memory=self.memory,
        )

    def chat(
        self,
        user_message: str,
    ) -> str:
        """
        Process a user message.
        """

        self.memory.save_message(
            role="user",
            content=user_message,
        )

        history = self.memory.get_recent_messages(20)

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

        response = self.chat_manager.chat(messages)

        self.memory.save_message(
            role="assistant",
            content=response,
        )

        return response