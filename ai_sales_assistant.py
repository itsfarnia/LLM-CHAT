from openai import OpenAI

client = OpenAI()

business = input("What do you sell? ")

prompt = f"""
You are a high-level sales expert.

The user sells:
{business}

Generate:

1. A powerful sales pitch
2. A short cold outreach message
3. 3 common objections + responses
4. A strong closing line

Keep it persuasive, clear, and realistic.
"""

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

print(response.output_text)