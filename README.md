# COGS 109 Final Project: Air Quality and Health Impact

## Research Question

How do air quality metrics and weather conditions impact human health outcomes?

## Project Overview

This project analyzes the relationship between air quality, weather conditions, and public health outcomes using the Air Quality and Health Impact Dataset from Kaggle. The dataset contains 5,811 records with air quality metrics, pollutant concentrations, weather variables, and health outcome variables.

The main outcome variables are:

- `HealthImpactScore`: continuous health impact score from 0 to 100
- `HealthImpactClass`: categorical health impact class

## Repository Structure

```text
data/
  raw/                 Original dataset
  processed/           Cleaned or transformed datasets
docs/                  Project proposal and written materials
notebooks/             Jupyter notebooks for exploration and modeling
outputs/
  figures/             Generated plots
  tables/              Generated summary tables
src/                   Reusable Python scripts
```

## Planned Analysis

- Explore the dataset structure, missing values, and class distribution.
- Visualize relationships between pollution/weather variables and health outcomes.
- Fit regression models for continuous outcomes such as `HealthImpactScore`.
- Fit classification models for `HealthImpactClass`.
- Compare models using cross-validation and appropriate metrics.

## Important Modeling Notes

- Do not use `RecordID` as a predictor.
- Do not use `HealthImpactScore` as a predictor when modeling `HealthImpactClass`, because that can cause target leakage.
- `HealthImpactClass` is imbalanced, so classification should be evaluated with metrics beyond accuracy, such as precision, recall, F1-score, and confusion matrices.

## Getting Started

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the starter data summary:

```bash
python src/eda_summary.py
```

