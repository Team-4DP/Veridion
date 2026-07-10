from llm.hf_client import ask_ai


while True:

    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    answer = ask_ai(user_input)

    print("\nAtlas:", answer)