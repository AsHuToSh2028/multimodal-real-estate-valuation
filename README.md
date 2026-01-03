# Multimodal Real Estate Valuation  
**Tabular + Satellite Imagery Based Property Price Prediction**

## Overview
This repository implements a **multimodal real estate valuation system** that predicts residential property prices by combining **engineered tabular features** with **neighbourhood-level satellite imagery**.

The project was developed as part of the **CDC Open Project (2025–26)** at **IIT Roorkee**, with the objective of evaluating whether visual urban context (roads, greenery, density, built form) can enhance traditional Automated Valuation Models (AVMs) based on structured housing attributes.

A strong **tabular CatBoost baseline** is established through extensive feature engineering and hyperparameter optimisation. High-level visual embeddings are extracted from satellite images using **EfficientNet-B4** and fused with tabular features in a controlled multimodal experiment. Model behaviour is interpreted using **feature importance, surrogate trees, and Grad-CAM**.

---

## Key Objectives
- Build a robust **tabular baseline** for house price prediction  
- Programmatically fetch **satellite imagery** using latitude–longitude coordinates  
- Extract **CNN-based visual embeddings** from satellite tiles  
- Fuse image and tabular features in a **multimodal regression framework**  
- Compare **tabular-only vs. multimodal performance**  
- Ensure **model explainability** using Grad-CAM and interpretable surrogates  

---

## Repository Structure
multimodal-real-estate-valuation/
│
├── data_fetcher.py # Script to download satellite images using lat/long
├── Tabular_Only_Model.ipynb # EDA, feature engineering, and optimized CatBoost model
├── Multi_Model.ipynb # Multimodal pipeline (tabular + image embeddings)
├── 24113026_final.csv # Final test set predictions (id, predicted_price)
├── 24113026_report.pdf # Detailed project report (PDF)
├── README.md # Project documentation


---

## Dataset
**Base Dataset**
- Source: King County Housing Dataset  
- Key features:
  - `price` (target)
  - `bedrooms`, `bathrooms`
  - `sqft_living`, `sqft_lot`
  - `grade`, `condition`, `view`, `waterfront`
  - `lat`, `long`
  - neighbourhood aggregates (`sqft_living15`, `sqft_lot15`)

**Visual Data**
- Satellite images fetched using **Google Maps Static API**
- Resolution after preprocessing: **224×224 RGB**
- Visual cues captured:
  - vegetation density
  - road networks
  - block structure
  - built-form density
  - neighbourhood layout

---

## Methodology

### 1. Tabular Modeling
- Extensive EDA and preprocessing
- Log-transformation of target variable
- Feature engineering:
  - interaction terms (e.g., `grade × sqft`)
  - neighbourhood-normalised ratios
  - temporal features (age, renovation)
  - geospatial K-Means clustering
- Model selection via GridSearchCV
- Final model: **CatBoost Regressor**
- Hyperparameter optimisation using **Optuna (TPE sampler)**

### 2. Image Embedding Extraction
- Pretrained **EfficientNet-B4** (ImageNet weights)
- Classifier head removed
- Penultimate layer used as **1792-D visual embedding**
- Embeddings aligned with property IDs

### 3. Multimodal Fusion
- Concatenation of:
  - engineered tabular features
  - EfficientNet-B4 embeddings
- Regression using the **same optimized CatBoost configuration**
- Controlled experiment to isolate the contribution of visual context

### 4. Explainability
- Feature importance analysis (CatBoost)
- Surrogate decision tree to approximate model logic
- **Grad-CAM visualisations** to highlight satellite regions influencing predictions

---

## Results Summary

| Model | RMSE (log) | R² |
|------|-----------|----|
| Tabular CatBoost | **0.1597** | **0.9076** |
| Multimodal (Tabular + Images) | 0.1639 | 0.9026 |

**Key Insight:**  
Structured housing attributes explain the majority of price variance. Satellite imagery contributes meaningful neighbourhood context and interpretability but offers limited incremental predictive gain—consistent with findings in real-estate econometrics and industry AVMs (e.g., Zillow, Redfin).

---

## Files of Interest
- **`24113026_report.pdf`**  
  Full technical report with EDA, modelling details, architecture diagrams, and interpretability analysis.
- **`24113026_final.csv`**  
  Final prediction file submitted for evaluation.
- **`data_fetcher.py`**  
  Script for reproducible satellite image acquisition.

---

## Tech Stack
- **Data:** Pandas, NumPy, GeoPandas  
- **ML:** CatBoost, Scikit-learn, Optuna  
- **Deep Learning:** PyTorch, EfficientNet  
- **Vision:** OpenCV, PIL  
- **Explainability:** Grad-CAM, surrogate trees  
- **Visualization:** Matplotlib, Seaborn  

---

## Notes
- The project prioritizes **scientific correctness, interpretability, and reproducibility** over leaderboard-only optimisation.
- The multimodal setup mirrors real-world AVMs, where imagery acts as a contextual enhancer rather than a replacement for structured data.

---

## Author
**Ashutosh Gupta**  
IIT Roorkee  
Multimodal Machine Learning | Data Science
