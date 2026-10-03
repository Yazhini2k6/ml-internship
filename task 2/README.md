# Task 2 - Restaurant Recommendation System

Beginner-friendly machine learning project for the Restaurant Recommendation task.

## Independent-file design

Every Python file is independent. No project Python file imports another project Python file. Each script reads `data/restaurants.csv` itself and can be run directly from the project root.

## Structure

```text
Task2_Restaurant_Recommendation/
├── data/
│   └── restaurants.csv
├── preprocessing.py
├── recommender.py
├── evaluation.py
├── main.py
├── requirements.txt
└── README.md
```

## Files

- `preprocessing.py`: handles missing values and demonstrates categorical encoding.
- `recommender.py`: implements content-based filtering with TF-IDF and cosine similarity and prints recommendations.
- `evaluation.py`: independently generates recommendations and calculates Precision@K.
- `main.py`: independently demonstrates the complete Task 2 workflow.
- `requirements.txt`: Python dependencies.
- `data/restaurants.csv`: supplied restaurant dataset.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run any file independently

```bash
python preprocessing.py
python recommender.py
python evaluation.py
python main.py
```

No UI is included because the provided task requirements focus on the ML/recommendation system.

## ML techniques

- Missing-value handling
- Categorical encoding
- Feature engineering
- TF-IDF
- Cosine similarity
- Content-based filtering
- Precision@K evaluation
