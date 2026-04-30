from openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a professional, concise AI assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "clear":
        messages = messages[:1]
        print("Memory cleared.")
        continue

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input=messages
        )

        ai_reply = response.output_text
        print("AI:", ai_reply)

    except Exception as e:
        print("Error:", e)
        continue

    messages.append({"role": "assistant", "content": ai_reply})