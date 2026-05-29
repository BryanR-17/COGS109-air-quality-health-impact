from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "air_quality_health_impact_data.csv"
TABLES_DIR = ROOT / "outputs" / "tables"


def main() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:")
    print(df.shape)
    print()

    print("Columns:")
    print(list(df.columns))
    print()

    print("Missing values by column:")
    print(df.isna().sum())
    print()

    print("HealthImpactClass distribution:")
    class_counts = df["HealthImpactClass"].value_counts().sort_index()
    print(class_counts)
    print()

    predictors = [
        "AQI",
        "PM10",
        "PM2_5",
        "NO2",
        "SO2",
        "O3",
        "Temperature",
        "Humidity",
        "WindSpeed",
        "RespiratoryCases",
        "CardiovascularCases",
        "HospitalAdmissions",
    ]

    correlations = (
        df[predictors + ["HealthImpactScore", "HealthImpactClass"]]
        .corr(numeric_only=True)[["HealthImpactScore", "HealthImpactClass"]]
        .drop(index=["HealthImpactScore", "HealthImpactClass"])
        .sort_values("HealthImpactScore", ascending=False)
    )

    output_path = TABLES_DIR / "starter_correlations.csv"
    correlations.to_csv(output_path)

    print("Correlations with outcome variables:")
    print(correlations.round(3))
    print()
    print(f"Saved correlation table to: {output_path}")


if __name__ == "__main__":
    main()

