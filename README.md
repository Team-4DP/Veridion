# clanker-ai
PLEASE VIEW IN CODE FORM INSTEAD OF PREVIEW!!! This is just beause the charts don't work in preview. Thank you.
This is my new project, just licenced under Team-4DP, it is an AI chatbot I have made myself. The plan going forwards from here (version 0.1 beta at this moment in time).
Current structure:                      │    What is currently happening beind the scenes:
Clanker-AI                              │                      User
│                                       │                       ↓
├── config.py                           │                    main.py
├── main.py                             │                       ↓
├── llm/                                │                    ask_ai()
│      hf_client.py                     │                       ↓
│                                       │                  HuggingFace
└── memory/                             │                       ↓
       sqlite_memory.py                 │                    Quen 2.5
                                        │                       ↓
                                        │                    Response
                                        │
