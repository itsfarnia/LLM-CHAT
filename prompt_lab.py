from openai import OpenAI

client = OpenAI()

question = "How can I learn AI faster?"

personas = [
    "You are a strict teacher. Answer in 3 bullet points max.",
    "You are a motivational coach. Answer in 3 bullet points max.",
    "You are a business CEO. Answer in 3 bullet points max.",
    "You are an AI engineer. Answer in 3 bullet points max."
]

for persona in personas:
    print("\n-----------------------------")
    print("PERSONA:", persona)

    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {"role": "system", "content": persona},
            {"role": "user", "content": question}
        ]
    )

    print("AI:", response.output_text)