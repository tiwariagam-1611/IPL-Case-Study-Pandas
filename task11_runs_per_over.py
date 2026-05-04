import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

runs_per_over = (
    merged_df
    .groupby("over")["total_runs_calculated"]
    .mean()
    .reset_index()
    .rename(columns={"total_runs_calculated": "avg_runs"})
    .sort_values(by="over")
)

print(runs_per_over)

runs_per_over.to_csv("output/runs_per_over.csv", index=False)