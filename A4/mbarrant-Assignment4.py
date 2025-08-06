import json
import string
import numpy as np
import scipy.linalg
scipy.linalg.triu = np.triu
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from corpus import corpus
from sklearn.feature_extraction.text import TfidfVectorizer
import gensim
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors






# ****************


# This file contains questions 1-3 ONLY


# ******************

# Custom stopwords (problem-specific list)
stop_words = {"the", "and", "of", "in", "a", "to", "is", "it", "you", "for", 
"on", "with", "this", "that", "are", "as", "be"}

def preprocess(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Lowercase
    text = text.lower()
    # Split and filter
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    # Rejoin with spaces
    return ' '.join(filtered_words)


# 1)

# Load data
with open('JEOPARDY_QUESTIONS.json') as f:
    data = json.load(f)
    questions = [item['question'] for item in data[:10000]]


preprocessed_questions = [preprocess(q) for q in questions]

# One-hot encoding
vectorizer = CountVectorizer(binary=True)
one_hot_encoded = vectorizer.fit_transform(preprocessed_questions)

# # Output shape and example
print(f"One-hot encoded matrix shape: {one_hot_encoded.shape}")
print("Example vector:", one_hot_encoded[0].toarray())


# # Calculate cosine similarities
similarity_matrix = cosine_similarity(one_hot_encoded)

# # Find most similar pair (excluding identical ones)
n = similarity_matrix.shape[0]
rows, cols = np.triu_indices(n, k=1)
upper_similarities = similarity_matrix[rows, cols]

mask = upper_similarities < 1.0 - 1e-8
eligible_pairs = upper_similarities[mask]

if eligible_pairs.size == 0:
    print("No eligible pairs found.")
else:
    max_idx = np.argmax(eligible_pairs)
    max_sim = eligible_pairs[max_idx]
    i, j = rows[mask][max_idx], cols[mask][max_idx]
    
    print(f"\nMost Similar Pair (Score: {max_sim:.4f}):")
    print(f"Q1: {questions[i]}")
    print(f"Q2: {questions[j]}")


# # 2) 

preprocessed_docs = [preprocess(docs) for docs in corpus]

#TF-IDF calcculation
vectorizer2 = TfidfVectorizer(lowercase=False, stop_words=None)
tfidf_matrix = vectorizer.fit_transform(preprocessed_docs)
feature_names = vectorizer.get_feature_names_out()

# Extract top 4 keywords per document
keywords_per_doc = []
for i in range(tfidf_matrix.shape[0]):
    scores = tfidf_matrix[i].toarray().flatten()
    top_indices = np.argsort(scores)[::-1][:4]
    keywords = [feature_names[idx] for idx in top_indices]
    keywords_per_doc.append(keywords)

# Print results
for idx, keywords in enumerate(keywords_per_doc):
    print(f"Document {idx+1}: {keywords}")



# 3)

#word2vec format
glove_input = "glove.6B.300d.txt"
word2vec_output = "glove.6B.300d.word2vec.txt"
glove2word2vec(glove_input, word2vec_output)

#Load embeddings
glove_model = KeyedVectors.load_word2vec_format(word2vec_output, binary=False)

#Cmvert questions to Embeddigns
def question_to_vectors(question):
    vectors = []
    for word in question:
        if word in glove_model:
            vectors.append(glove_model[word])
    if len(vectors) == 0:
        return np.zeros(glove_model.vector_size)
    return np.mean(vectors, axis=0)

preprocessed_questions2 = [preprocess(q) for q in questions]
question_vectors = np.array([question_to_vectors(q) for q in preprocessed_questions2])

similarity_matrix = cosine_similarity(question_vectors)

# # A)
# # Find most similar pair (excluding identical)
# n = similarity_matrix.shape[0]
# rows, cols = np.triu_indices(n, k=1)
# upper_similarities = similarity_matrix[rows, cols]

# mask = upper_similarities < 1.0 - 1e-8
# eligible_pairs = upper_similarities[mask]

# if eligible_pairs.size > 0:
#     max_idx = np.argmax(eligible_pairs)
#     i, j = rows[mask][max_idx], cols[mask][max_idx]
#     max_sim = eligible_pairs[max_idx]
    
#     print(f"Most Similar Pair (Embedding Score: {max_sim:.4f}):")
#     print(f"Q1: {questions[i]}")
#     print(f"Q2: {questions[j]}")


