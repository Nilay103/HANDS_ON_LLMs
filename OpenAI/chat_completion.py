from azure_connector import azure_openai_connector


# Example 1
chat_completion = azure_openai_connector.send_message(
    messages=[{"role": "user", "content": "Listen to your"}],
    **{"max_tokens": 1, "temperature": 0, "n": 1}
)
print("-"*10)
print(chat_completion.choices[0].message.content)

# Example 2
chat_completion = azure_openai_connector.send_message(
    messages=[{"role": "user", "content": "Listen to your"}],
    **{"max_tokens": 10, "temperature": 1, "n": 1}
)
print("-"*10)
print(chat_completion.choices[0].message.content)

# Example 3
chat_completion = azure_openai_connector.send_message(
    messages=[{"role": "user", "content": "Listen to your"}],
    **{"max_tokens": 10, "temperature": 2, "n": 1}
)
print("-"*10)
print(chat_completion.choices[0].message.content)

# Example 4
chat_completion = azure_openai_connector.send_message(
    messages=[{"role": "user", "content": "Listen to your"}],
    **{"max_tokens": 10, "temperature": 0, "n": 5}
)
print("-"*10)
for i in range(len(chat_completion.choices)):
    print(chat_completion.choices[i].message.content)

# Example 5
chat_completion = azure_openai_connector.send_message(
    messages=[{"role": "user", "content": "Listen to your"}],
    **{"max_tokens": 10, "temperature": 2, "n": 5}
)
print("-"*10)
for i in range(len(chat_completion.choices)):
    print(chat_completion.choices[i].message.content)
