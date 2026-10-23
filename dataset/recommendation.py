
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the preprocessed dataset
df = pd.read_csv("ted_talks_preprocessed.csv")

# 2. Handle any missing combined text
df["combined_text"] = df["combined_text"].fillna("")

# 3. Convert text into numerical TF-IDF vectors
tfidf = TfidfVectorizer(stop_words="english", max_features=10000)
tfidf_matrix = tfidf.fit_transform(df["combined_text"])

# 4. Calculate similarity between TED Talks
similarity_matrix = cosine_similarity(tfidf_matrix)

print("TF-IDF model created successfully!")
print("Number of TED Talks:", len(df))
print("TF-IDF matrix shape:", tfidf_matrix.shape)
print("Similarity matrix shape:", similarity_matrix.shape)

def recommend_talks(talk_title, top_n=5):
    # Find the selected TED Talk
    matches = df[df["title"].str.lower() == talk_title.lower()]

    if matches.empty:
        print("TED Talk not found. Please check the title.")
        return

    talk_index = matches.index[0]

    # Get similarity scores for the selected talk
    scores = list(enumerate(similarity_matrix[talk_index]))

    # Sort from most similar to least similar
    scores = sorted(scores, key=lambda item: item[1], reverse=True)

    # Exclude the selected talk itself
    scores = [item for item in scores if item[0] != talk_index]

    print("\nRecommended TED Talks:\n")

    for index, score in scores[:top_n]:
        print(f"Title: {df.iloc[index]['title']}")
        print(f"Similarity: {score * 100:.2f}%")
        print("-" * 50)


# Test the recommendation system
recommend_talks(df.iloc[0]["title"])
recommend_talks("How to run a company with (almost) no rules")