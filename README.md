# Personalized TED Talks Recommendation System

## Project Overview
This project recommends relevant TED Talks using Python and machine learning techniques. It uses TF-IDF vectorization and cosine similarity to identify talks with similar textual content.

## Objectives
- Explore and clean TED Talks metadata and transcripts.
- Perform exploratory data analysis (EDA).
- Preprocess text for recommendation.
- Recommend talks based on content similarity.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TF-IDF
- Cosine Similarity
  
## Project Structure
- `dataset/` — Dataset files and recommendation script
  - `ted_main.csv` — TED Talks metadata
  - `transcripts.csv` — TED Talks transcripts
  - `dataset/recommendation.py` — Content-based recommendation logic
- `explore_dataset.py` — Data merging, cleaning, preprocessing, and EDA
- `ted_talks_preprocessed.csv` — Preprocessed dataset
- `dataset_documentation.md` — Dataset and column documentation
- `talk_length_distribution.png` — Talk duration visualization
- `tag_frequency.png` — Topic tag visualization
  
## Current Progress
- Dataset merging and cleaning
- Missing-data handling
- Text preprocessing
- Exploratory data analysis
- TF-IDF-based content similarity recommendations

## How It Works
1. Load the preprocessed TED Talks dataset.
2. Convert text into TF-IDF features.
3. Calculate cosine similarity between talks.
4. Display recommendations for a selected talk.

## Future Enhancements
- Evaluate recommendation quality using suitable metrics.
- Explore user preferences and feedback where data is available.
- Develop a Streamlit web application.

## Author
Viyas S
