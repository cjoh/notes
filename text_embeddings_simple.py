# Text Embeddings Explanation - Simple Example

# What are text embeddings?
# They are numerical representations (vectors) of text that capture semantic meaning

# Example embeddings (simplified - real ones have hundreds of dimensions)
embeddings = {
    "I love programming": [0.8, 0.2, 0.5],
    "I enjoy coding": [0.7, 0.3, 0.6],
    "I like to write software": [0.75, 0.25, 0.55],
    "I hate bugs": [0.3, -0.5, 0.4],
    "The weather is nice": [-0.2, 0.8, -0.3]
}

# Simple cosine similarity calculation
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sum(a * a for a in vec1) ** 0.5
    norm2 = sum(b * b for b in vec2) ** 0.5
    return dot_product / (norm1 * norm2)

print("Text Embedding Similarities:\n")
sentences = list(embeddings.keys())

# Compare all sentences
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        sent1, sent2 = sentences[i], sentences[j]
        similarity = cosine_similarity(embeddings[sent1], embeddings[sent2])
        print(f'"{sent1}" vs "{sent2}"')
        print(f"Similarity: {similarity:.3f}\n")

print("\nKey Properties of Text Embeddings:")
print("1. Similar texts have vectors that are close together")
print("2. The distance/angle between vectors represents semantic similarity")
print("3. They enable mathematical operations on text (addition, similarity, etc.)")
print("4. Modern models create embeddings with 256-1536+ dimensions")
print("5. They capture context, meaning, and relationships between words/sentences")