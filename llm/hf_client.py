from huggingface_hub import InferenceClient
from config import HF_TOKEN


client = InferenceClient(
    token=HF_TOKEN
)


def ask_ai(message):

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
    )

    return response.choices[0].message.content