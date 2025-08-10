## California Housing Price Predictor
A Flask-based web application that predicts California house prices based on multiple input factors such as median income, house age, average rooms, average bedrooms, and population. Powered by Linear Regression.

## Table of Contents
- Overview
- Features
- Tech Stack
- Installation
- Usage
- Project Structure
- Dataset
- Screenshots
- License

---

## Overview
This project uses **Linear Regression** to estimate the median house value in different regions of California.  
It is designed for quick and reliable price estimation based on five real-world housing features from the California Housing dataset.

---

## Features
- Takes **5 user inputs** related to housing and demographics
- Predicts house prices in **USD**
- Simple, responsive UI with styled input fields
- Model trained on **California Housing dataset** from scikit-learn
- Easy to run locally with Flask

---

## Project Structure
```
california-housing-predictor/
│
├── app.py                          # Main Flask app
├── model.py                        # Model training script
├── multi_feature_house_model.pkl   # Saved regression model
├── templates/
│   └── index.html                   # Frontend HTML
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## Tech Stack
| Technology     | Use |
|----------------|-----|
| Python         | Core language |
| Flask          | Web framework |
| scikit-learn   | ML modeling |
| HTML/CSS       | Frontend UI |
| Pandas         | Data handling |
| NumPy          | Numerical operations |
| Joblib         | Model persistence |

---

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/<your-username>/california-housing-predictor.git
cd california-housing-predictor
pip install -r requirements.txt
```

Train the model:
```bash
python model.py
```

Run the Flask server:
```bash
python app.py
```

Open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## Dataset
**Source:** California Housing Dataset (available in scikit-learn)

**Selected Features:**
- Median Income (MedInc) — Median income in $10,000's
- House Age (HouseAge) — Median age of houses
- Average Rooms (AveRooms) — Average rooms per household
- Average Bedrooms (AveBedrms) — Average bedrooms per household
- Population — Population of the block group

**Target Variable:**
- Median House Value (in USD)

---

## Screenshots

![alt text](<Screenshot_1.png>)
![alt text](<Screenshot_2.png>)
![alt text](<Screenshot_3.png>)

---
