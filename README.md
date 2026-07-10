# clanker-ai
PLEASE VIEW IN CODE FORM INSTEAD OF PREVIEW!!! This is just beause the charts don't work in preview. Thank you.
This is my new project, just licenced under Team-4DP, it is an AI chatbot I have made myself. Please feel free to fork this repository and use it. If there are any issues, please tell me and/or bring it up in the issues tab, i will try to help. As far as im aware, this uses gihub's codespace feature to host the AI instead of using your own hardware. Bring any suggestion like a downloadable offline version that does run on your own hardware or any extra features that are not mentioned in the roadmap below in the discussions tab. The plan going forwards from here (version 0.1 beta at this moment in time) is shown below, along with a quick start up guide.
       Current structure:               │    What is currently happening beind the scenes:
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
Roadmap for future progress:
v0.2
- Better chat loop
- Conversation memory
- Config system
v0.3
- Web search
- File tools
- Logging
v0.4
- Repository indexing
- Code understanding
v0.5
- Autonomous coding agent
v0.6
- Long-term memory
v0.7
- Personal AI development assistant
   ↓
v1.0
- Not sure yet (will be updated closer to the time)

Long Term Roadmap:(in order, mainly)
Clean(er) architecture
SQLite memory
Actual chat interface (instead of just a basic terminal chat)
Web search
Tool calling
File reading
Project understanding
Repository indexing
Semantic search
Coding agent
Terminal execution
Python execution
Auto debugging
Long-term memory
Vector database
Embeddings
Multi-agent architecture
Planner
Researcher
Coder
Game Design module
Plugins(and hopefully artifacts)
Full AI development assistant that is on par with modern AI's, but is completely open source and free to use.(Might change depending on how successful this is,just saying =) =) =)
Quick start guide to using Clanker AI
