# TED Talks Dataset Documentation

## 1. Project

**Project title:** Personalized TED Talks Recommendation System Using Machine Learning

This project recommends TED Talks that are textually similar to a selected talk. The recommendation script reads `ted_talks_preprocessed.csv` and uses TF-IDF text features and cosine similarity.

## 2. Dataset description

The preprocessed dataset contains **2,550 rows and 21 columns**. Each row represents a TED Talk record. The dataset includes talk metadata, speaker information, topic tags, transcripts, and derived text fields used by the recommendation system.

**Dataset used by the recommendation code:** `ted_talks_preprocessed.csv`

**Main recommendation input:** `combined_text`

The `explore_dataset.py` script creates the combined text from the talk title, description, readable tags, and transcript. The recommendation script converts this text into TF-IDF features and compares talks using cosine similarity.

## 3. Column descriptions

| Column | Description |
|---|---|
| `comments` | Number of comments associated with the talk. |
| `description` | Text summary or description of the talk. |
| `duration` | Talk duration in seconds. |
| `event` | Event at which the talk was presented. |
| `film_date` | Numeric timestamp representing the filming date. |
| `languages` | Number of languages in which the talk is available. |
| `main_speaker` | Name of the main speaker. |
| `name` | Talk name as recorded in the source dataset. |
| `num_speaker` | Number of speakers associated with the talk. |
| `published_date` | Numeric timestamp representing the publication date. |
| `ratings` | Rating information associated with the talk. |
| `related_talks` | Metadata identifying related talks. |
| `speaker_occupation` | Speaker's occupation. |
| `tags` | Original topic tags associated with the talk. |
| `title` | Talk title; used to look up a talk for recommendations. |
| `url` | URL of the TED Talk. |
| `views` | Number of views recorded for the talk. |
| `transcript` | Text transcript of the talk. |
| `duration_minutes` | Derived duration in minutes, calculated from `duration` in seconds. |
| `tags_text` | Topic tags converted into readable text. |
| `combined_text` | Lowercase text combined from the title, description, readable tags, and transcript; used for TF-IDF processing. |

## 4. Data quality observations

The uploaded preprocessed CSV was checked for its basic structure and data quality:

- **Rows:** 2,550
- **Columns:** 21
- **Missing values in `transcript`:** 86
- **Missing values in the other 20 columns:** 0
- **Fully duplicated rows:** 0
- **Duplicate URLs:** 0
- **Missing values in `combined_text`:** 0

These checks describe the uploaded CSV file. If the dataset is regenerated or changed, run the checks again and update this section if the results differ.

## 5. Missing-data mitigation

- The `explore_dataset.py` script fills missing `transcript` values with an empty string before creating the preprocessed text output.
- The recommendation script also applies `fillna("")` to `combined_text` as a safeguard before TF-IDF processing.
- An empty transcript means transcript content is unavailable for that record; the model may still use the title, description, and tags if those fields contain text.
- Do not replace missing transcripts with invented text.

## 6. Other preprocessing and handling

- Duplicate transcript URLs are removed before merging in the exploration script.
- Missing `speaker_occupation` values are filled with `Unknown` in the exploration script.
- `duration_minutes` is derived from the original `duration` value in seconds.
- `tags_text` provides a readable text representation of tags.
- `combined_text` combines the title, description, tags, and transcript in lowercase.
- The recommendation script uses `TfidfVectorizer(stop_words="english", max_features=10000)`.
- Cosine similarity is calculated between the TF-IDF vectors to rank similar talks.
- Similarity scores are text-similarity scores; they are **not** model accuracy.

## 7. Scope and Future Enhancements

- **Text-based recommendations:** The system recommends TED Talks based on similarities in titles, descriptions, tags, and transcripts.
- **Transcript availability:** When a transcript is unavailable, the system can still use other available text fields to generate recommendations.
- **Personalization:** Future versions could incorporate user interests and feedback to provide more personalized recommendations.
- **Recommendation evaluation:** Future work could include user feedback and evaluation metrics to assess recommendation relevance.
- **Dataset updates:** Updating the dataset periodically can help keep talk information current.

## 8. Files in the workflow

- `ted_main.csv`: original TED Talk metadata.
- `transcripts.csv`: transcript data.
- `ted_talks_merged.csv`: merged dataset.
- `ted_talks_preprocessed.csv`: preprocessed dataset read by `recommendation.py`.
- `explore_dataset.py`: exploration, cleaning, and preprocessing script.
- `recommendation.py`: TF-IDF and cosine-similarity recommendation script.
