import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

city_runs = (
    merged_df
    .groupby("city")["total_runs_calculated"]
    .mean()
    .reset_index()
    .rename(columns={"total_runs_calculated": "avg_runs"})
    .sort_values(by="avg_runs", ascending=False)
)

print(city_runs.head())

city_runs.to_csv("output/city_trends.csv", index=False)