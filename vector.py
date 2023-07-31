import numpy as np
from gensim.models import KeyedVectors
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

# Load word vectors
word_vectors = KeyedVectors.load_word2vec_format('glove-wiki-gigaword-300.txt')

# Sentence similarity scores
sentence_scores = {}


def calculate_sentence_score(sentence):
    # Remove stop words
    sentence = [w for w in sentence.lower().split() if w not in stop_words]

    # Look up word embeddings
    word_embeddings = [word_vectors[w] for w in sentence if w in word_vectors]

    # Take average to get sentence embedding
    sentence_embedding = np.mean(word_embeddings, axis=0)

    # Calculate similarity to other sentences
    for other_sentence, other_embedding in sentence_scores.items():
        cos_sim = cosine_similarity(sentence_embedding.reshape(1, -1), other_embedding.reshape(1, -1))
        sentence_scores[(sentence, other_sentence)] = cos_sim

    # Add current sentence to dictionary
    sentence_scores[sentence] = sentence_embedding


# Calculate score for a new sentence
new_sentence = "The sky is blue"
calculate_sentence_score(new_sentence)

# Get most similar sentence
most_similar = max(sentence_scores.items(), key=operator.itemgetter(1))[0]
print(most_similar)  # "The ocean is blue"