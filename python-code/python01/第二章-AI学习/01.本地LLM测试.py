from ollama import chat

prompt = {'role': 'system', 'content': '你的名字叫Jack，是一名说话简洁的AI助理，你会尽量简单的回答任何问题'}
memory = {'role': 'assistant', 'content': ''}
message = [prompt]
while True:
    user = {'role': 'user', 'content': input("用户: ")}
    if user.get('content') == '/88':
        break

    message.append(user)

    response = chat(model='gemma4', messages=message)

    memory['content'] = response.message.content

    print(f"AI助手: {response.message.content}")
    message.append(memory)
