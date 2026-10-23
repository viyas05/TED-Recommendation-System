
import pandas as pd

# Load the TED Talks dataset
df = pd.read_csv("dataset/ted_main.csv")

# Display the first five rows
print("First 5 rows:")
print(df.head())

# Display column names
print("\nDataset Columns:")
print(df.columns.tolist())

# Display dataset size
print("\nDataset Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\n--- Transcript Dataset ---")

transcripts = pd.read_csv("dataset/transcripts.csv")

print("First 5 rows:")
print(transcripts.head())

print("\nTranscript columns:")
print(transcripts.columns.tolist())

print("\nTranscript dataset size:")
print(transcripts.shape)

print("\nMissing values:")
print(transcripts.isnull().sum())

# Match the main dataset with the transcript dataset
merged = pd.merge(
    df,
    transcripts,
    on="url",
    how="left"
)

print("\n--- Merged Dataset ---")
print("Total rows:", merged.shape[0])
print("Total columns:", merged.shape[1])

print("\nMissing transcripts:")
print(merged["transcript"].isnull().sum())

print("\nSample talk with transcript:")
print(merged[["title", "main_speaker", "transcript"]].head(2))

# Save the merged dataset
merged.to_csv("dataset/ted_talks_merged.csv", index=False)

print("\nMerged dataset saved successfully!")

print("\n--- URL Duplicate Check ---")

print("Main dataset duplicate URLs:",
      df["url"].duplicated().sum())

print("Transcript duplicate URLs:",
      transcripts["url"].duplicated().sum())

print("Unique transcript URLs:",
      transcripts["url"].nunique())

# Remove duplicate URLs from the transcript dataset
transcripts_unique = transcripts.drop_duplicates(
    subset="url",
    keep="first"
)

# Merge the datasets
merged = pd.merge(
    df,
    transcripts_unique,
    on="url",
    how="left",
    validate="one_to_one"
)

print("\n--- Final Merged Dataset ---")
print("Total rows:", merged.shape[0])
print("Total columns:", merged.shape[1])
print("Missing transcripts:", merged["transcript"].isnull().sum())

# Save the merged dataset
merged.to_csv("dataset/ted_talks_merged.csv", index=False)

print("Merged dataset saved successfully!")

# Handle missing values

# Fill missing speaker occupations
merged["speaker_occupation"] = merged["speaker_occupation"].fillna("Unknown")

# Check missing values
print("\nMissing values after handling:")
print(merged.isnull().sum())

# Save the dataset
merged.to_csv("dataset/ted_talks_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
# Check duplicate URLs in the merged dataset
print("\n--- Duplicate URL Check ---")

print("Total rows:", len(merged))
print("Unique URLs:", merged["url"].nunique())
print("Duplicate URLs:", merged["url"].duplicated().sum())
# Display duplicate transcript URLs
print("\n--- Duplicate Transcript URLs ---")

duplicates = transcripts[
    transcripts["url"].duplicated(keep=False)
].sort_values("url")

print(duplicates[["url", "transcript"]].to_string(index=False))
# Investigate missing transcripts
print("\n--- Missing Transcript Analysis ---")

missing_transcripts = merged[merged["transcript"].isna()]

print("Missing transcript count:", len(missing_transcripts))

print("\nSample talks without transcripts:")
print(
    missing_transcripts[["title", "main_speaker", "tags"]]
    .head(10)
    .to_string(index=False)
)
# Handle missing transcripts
merged["transcript"] = merged["transcript"].fillna("")

print("Missing transcripts after cleaning:",
      merged["transcript"].isna().sum())

print("Final dataset shape:", merged.shape)

merged.to_csv("dataset/cleaned_ted_talks.csv", index=False)
print("Cleaned dataset saved successfully!")
import pandas as pd

df = pd.read_csv("dataset/cleaned_ted_talks.csv")

print("Dataset columns:")
print(df.columns.tolist())

print("\nTotal columns:", len(df.columns))
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("dataset/cleaned_ted_talks.csv")

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Sample TED Talks ---")
print(
    df[["title", "tags", "description", "transcript"]]
    .head(3)
    .to_string()
)
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

import ast
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load your final cleaned dataset
# Use the existing cleaned DataFrame
df["duration_minutes"] = df["duration"] / 60
df["transcript"] = df["transcript"].fillna("")

print("Missing transcripts:", df["transcript"].isna().sum())
print("Empty transcripts:",
      df["transcript"].str.strip().eq("").sum())

import ast
import matplotlib.pyplot as plt
from collections import Counter

# 1. Talk length distribution
df["duration_minutes"] = df["duration"] / 60

plt.figure(figsize=(9, 5))
plt.hist(df["duration_minutes"], bins=30, edgecolor="black")
plt.title("TED Talk Length Distribution")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Talks")
plt.tight_layout()
plt.savefig("talk_length_distribution.png")
plt.show()

# 2. Most frequent tags
tag_counts = Counter()

for value in df["tags"]:
    try:
        tags = ast.literal_eval(value) if isinstance(value, str) else value
        if isinstance(tags, list):
            tag_counts.update(str(tag).lower() for tag in tags)
    except (ValueError, SyntaxError):
        pass

top_tags = tag_counts.most_common(15)

if top_tags:
    labels, counts = zip(*top_tags)

    plt.figure(figsize=(10, 6))
    plt.barh(labels[::-1], counts[::-1], edgecolor="black")
    plt.title("Top 15 TED Talk Tags")
    plt.xlabel("Number of Talks")
    plt.ylabel("Tag")
    plt.tight_layout()
    plt.savefig("tag_frequency.png")
    plt.show()

print("Both EDA graphs generated successfully!")

print("\n===== FINAL DATA QUALITY SUMMARY =====")

print("Total TED Talks:", len(df))
print("Total columns:", df.shape[1])
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate URLs:", df["url"].duplicated().sum())
print("Missing values:\n", df.isnull().sum())
print("Empty transcripts:",
      df["transcript"].fillna("").str.strip().eq("").sum())

print("\n===== TALK STATISTICS =====")
print("Average duration (minutes):",
      round(df["duration"].mean() / 60, 2))
print("Median duration (minutes):",
      round(df["duration"].median() / 60, 2))
print("Average views:",
      round(df["views"].mean(), 2))

print("\nWeek 2 EDA summary completed!")

import ast

# Prepare text fields
for col in ["title", "description", "tags", "transcript"]:
    df[col] = df[col].fillna("").astype(str)

# Convert tags from list-like text into readable text
def process_tags(value):
    try:
        tags = ast.literal_eval(value)
        if isinstance(tags, list):
            return " ".join(str(tag) for tag in tags)
    except (ValueError, SyntaxError):
        pass
    return value

df["tags_text"] = df["tags"].apply(process_tags)

# Combine text for recommendation
df["combined_text"] = (
    df["title"] + " " +
    df["description"] + " " +
    df["tags_text"] + " " +
    df["transcript"]
).str.lower().str.strip()

# Save the dataset
df.to_csv("ted_talks_preprocessed.csv", index=False)

print("\nPreprocessed dataset saved!")
print("Dataset shape:", df.shape)
print("Empty combined text:", df["combined_text"].eq("").sum())
print("Output file: ted_talks_preprocessed.csv")
