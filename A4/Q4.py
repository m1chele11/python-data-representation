import nltk
import json 
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns
from itertools import combinations


# Load data
with open('JEOPARDY_QUESTIONS.json') as f:
    data = json.load(f)
    questions = [item['question'] for item in data[:10000]]

# 1)

# A)
# Assuming 'questions' is a list of preprocessed questions
all_words = ' '.join(questions).split()

# Count word frequencies
word_freq = Counter(all_words)
most_common = word_freq.most_common(20)

# Plot Bar Chart
words, counts = zip(*most_common)
plt.figure(figsize=(12, 6))
plt.bar(words, counts)
plt.xticks(rotation=45)
plt.title('Top 20 Most Frequent Words in Jeopardy Questions')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()


# B)
# Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(all_words))

# Plot Word Cloud
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Jeopardy Questions Word Cloud')
plt.show()


# C)

# Get unique words
unique_words = [word for word, _ in most_common]
co_occurrence = pd.DataFrame(0, index=unique_words, columns=unique_words)

# Build co-occurrence matrix
for question in questions:
    tokens = set(question.split())
    for word1, word2 in combinations(tokens, 2):
        if word1 in unique_words and word2 in unique_words:
            co_occurrence.at[word1, word2] += 1
            co_occurrence.at[word2, word1] += 1

# Plot Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(co_occurrence, cmap='Blues')
plt.title('Word Co-occurrence Heatmap')
plt.show()
