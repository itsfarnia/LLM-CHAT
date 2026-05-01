from openai import OpenAI

client = OpenAI()

with open("notes.txt", "r", encoding="utf-8") as file:
    document = file.read()

# تقسیم متن به تکه‌های کوچیک
chunks = document.split(". ")

question = input("Ask a question about the file: ")

# انتخاب تکه‌های مرتبط
relevant_chunks = []
for chunk in chunks:
    if any(word.lower() in chunk.lower() for word in question.split()):
        relevant_chunks.append(chunk)

context = " ".join(relevant_chunks)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
"""

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

print("AI:", response.output_text)