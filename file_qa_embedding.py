from openai import OpenAI
import numpy as np

client = OpenAI()

# Create an embedding for a given text
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(response.data[0].embedding)

# Calculate cosine similarity between two vectors
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Read the document
with open("notes.txt", "r", encoding="utf-8") as file:
    document = file.read()

# Split the document into smaller chunks
chunks = document.split(". ")

# Create embeddings for all chunks once
chunk_embeddings = [get_embedding(chunk) for chunk in chunks]

while True:
    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    question_embedding = get_embedding(question)

    # Find the top 3 most relevant chunks
    scores = [cosine_similarity(question_embedding, emb) for emb in chunk_embeddings]
    top_indices = np.argsort(scores)[-3:]
    top_chunks = [chunks[i] for i in top_indices]
    context = " ".join(top_chunks)

    prompt = f"""
Answer strictly using the context below.
Do not add any extra knowledge.
If the answer is not found in the context, say "I don't know."

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