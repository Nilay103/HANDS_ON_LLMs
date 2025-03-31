from azure_connector import azure_openai_connector


messages = [
    {"role": "system", "content": "You are a lyric completion assistant. When given a line from a song, you will provide the next line in the song'"},
    {"role": "user", "content": "I've been reading books of old, the legends and the myths"},
    {"role": "assistant", "content": "Achilles and his gold, Hercules and his gifts"},
    {"role": "user", "content": "Spider-Man's control and Batman with his fists"},
    {"role": "assistant", "content": "And clearly, I don't see myself upon that list"},
]

for i in range(4):
    chat_completion = azure_openai_connector.send_message(
        messages=messages,
        **{"max_tokens": 50, "temperature": 0.7},
    )

    response = chat_completion.choices[0].message.content
    print(response)

    messages.append({"role": "assistant", "content": response})
