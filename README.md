# Personalized TED Talks Recommendation System Using Machine Learning

**Project Status:** In Progress  
**Program:** Infosys Springboard Virtual Internship 7.0

## 1. Project Overview

This project aims to recommend relevant TED Talks to users based on talk metadata, topics, descriptions, and transcripts. The project uses Python and machine learning techniques to develop a content-based recommendation system.

## 2. Objectives

- Collect and explore TED Talks metadata and transcripts.
- Clean and preprocess the dataset.
- Perform exploratory data analysis (EDA).
- Develop and evaluate recommendation techniques.
- Build an interactive application for TED Talk recommendations.
- Document the implementation and results.

## 3. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TF-IDF and cosine similarity (recommendation development)

## 4. Project Structure

- `dataset/` — Dataset files and recommendation script
  - `ted_main.csv` — TED Talks metadata
  - `transcripts.csv` — TED Talks transcripts
  - `recommendation.py` — Content-based recommendation implementation
  - `ted_talks_merged.csv` — Merged dataset
  - `ted_talks_cleaned.csv` — Cleaned dataset
  - `cleaned_ted_talks.csv` — Additional cleaned dataset
- `explore_dataset.py` — Dataset merging, cleaning, preprocessing, and EDA
- `ted_talks_preprocessed.csv` — Preprocessed dataset
- `dataset_documentation.md` — Dataset and column documentation
- `talk_length_distribution.png` — Talk duration visualization
- `tag_frequency.png` — Topic tag frequency visualization

## 5. Current Progress: Weeks 1–2

- Dataset collection and merging
- Data cleaning and preprocessing
- Missing-data handling
- Dataset quality checks
- Dataset and column documentation
- Talk duration distribution visualization
- Topic tag frequency visualization

## 6. Eight-Week Development Roadmap

- **Weeks 1–2:** Dataset collection, cleaning, preprocessing, EDA, and dataset documentation.
- **Weeks 3–4:** Feature engineering, vectorization, recommendation engine development, and saving model artifacts.
- **Weeks 5–6:** Recommendation evaluation using suitable metrics and comparison of approaches where applicable.
- **Weeks 7–8:** Streamlit application development, deployment documentation, final project report, and presentation.

## 7. How the Recommendation System Works

The planned content-based recommendation workflow is:

1. Load the preprocessed TED Talks dataset.
2. Convert textual content into numerical features using TF-IDF.
3. Calculate cosine similarity between talks.
4. Recommend talks with similar content.

## 8. Future Enhancements

- Improve recommendation quality.
- Evaluate recommendations using suitable metrics.
- Explore user preferences and feedback if interaction data is available.
- Develop an interactive Streamlit application.
- Complete the final project report and presentation.

## 9. Author

Viyas S
