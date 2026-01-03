# Multimodal Real Estate Valuation  
**Tabular + Satellite Imagery Based Property Price Prediction**

## Overview
This repository implements a **multimodal real estate valuation system** that predicts residential property prices by combining **engineered tabular features** with **neighbourhood-level satellite imagery**.

The project was developed as part of the **CDC Open Project (2025–26)** at **IIT Roorkee**, with the goal of evaluating whether visual urban context (roads, greenery, density, built form) can enhance traditional Automated Valuation Models (AVMs) based on structured housing attributes.

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
