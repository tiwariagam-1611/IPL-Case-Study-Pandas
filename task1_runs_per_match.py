import pandas as pd

merged_df = pd.read_csv("merged_data.csv")

runs_per_match = (
    merged_df
    .groupby("match_id")["total_runs_calculated"]
    .sum()
    .reset_index()
    .rename(columns={"total_runs_calculated": "total_runs"})
    .sort_values(by="total_runs", ascending=False)
)

print(runs_per_match.head())

runs_per_match.to_csv("output/runs_per_match.csv", index=False)