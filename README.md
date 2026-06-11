# COGS 109 Final Project: Air Quality and Health Impact

## Research Question

How do air quality metrics and weather conditions impact human health outcomes?

## Project Overview

This project analyzes relationships between air quality, weather conditions, and public health outcomes using the [Air Quality and Health Impact Dataset](https://www.kaggle.com/datasets/rabieelkharoua/air-quality-and-health-impact-dataset). The dataset contains 5,811 records and includes pollutant measurements, weather variables, and health impact indicators.

The primary outcome variables are:

- `HealthImpactScore`: a continuous health impact score from 0 to 100
- `HealthImpactClass`: a categorical health impact classification

## Repository Structure

```text
data/
  raw/                 Original dataset
docs/                  Project proposal and written materials
notebooks/             Exploratory analysis and model comparisons
```

## Notebooks

### `01_exploratory_analysis.ipynb`

Explores the dataset structure, missing values, class imbalance, correlations, and relationships between environmental variables and `HealthImpactScore`.

We found out that `HealthImpactClass` is imbalanced with most observations in class **0**, we randomly choose 650 samples from class 0 to reduce imbalanced. This value was chosen to be comparable to the size of the second-largest class while retaining sufficient training data. Models were then evaluated using Accuracy, Balanced Accuracy, and Macro F1-score, with Macro F1 serving as the primary metric because it gives equal weight to each class.

### `02_regression_models.ipynb`

Predicts `HealthImpactScore` using environmental variables. The notebook compares:

- Multiple Linear Regression
- Lasso Regression
- Polynomial Regression
- Principal Component Regression (PCR)

Models are selected using 10-fold cross-validation and evaluated on a held-out test set. Polynomial Regression with degree `3` performed best, with a test RMSE of approximately `2.304` and a test R-squared value of approximately `0.972`.

### `03_classification_models.ipynb`

Predicts `HealthImpactClass` using environmental variables. The notebook compares:

- Multiclass Logistic Regression
- Lasso-Regularized Logistic Regression
- K-Nearest Neighbors (KNN)

Among the models tested, KNN achieved the highest test accuracy (0.619) and balanced accuracy (0.365), while **Logistic Regression** achieved the highest macro F1-score (0.362). Because macro F1 places equal importance on all classes, **Logistic Regression** demonstrated the most balanced performance across the health impact categories and was therefore selected as the best overall classification model.

## Key Findings

- AQI had the strongest positive relationship with `HealthImpactScore` during exploratory analysis.
- Polynomial Regression substantially outperformed the linear, Lasso, and PCR regression models for predicting `HealthImpactScore`.
- Classification was more difficult because most observations belong to `HealthImpactClass` `0`.
- KNN achieved high overall accuracy but performed poorly on the least common classes.
- Logistic Regression produced the highest balanced accuracy, meaning it treated minority classes more evenly than KNN.

## Modeling Decisions

- `RecordID` was excluded because it is only an identifier.
- Environmental variables were used as predictors: `AQI`, `PM10`, `PM2_5`, `NO2`, `SO2`, `O3`, `Temperature`, `Humidity`, and `WindSpeed`.
- `HealthImpactScore` was excluded when predicting `HealthImpactClass` to avoid target leakage.
- Classification performance was evaluated using accuracy, balanced accuracy, macro F1-score, classification reports, and confusion matrices.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the notebooks in VS Code or Jupyter and run the cells from top to bottom.
