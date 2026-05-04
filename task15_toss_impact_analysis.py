import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

toss_runs = (
    merged_df
    .groupby(["match_id", "toss_winner"])["total_runs_calculated"]
    .sum()
    .reset_index()
)

toss_summary = (
    toss_runs
    .groupby("toss_winner")["total_runs_calculated"]
    .mean()
    .reset_index()
    .rename(columns={"total_runs_calculated": "avg_runs"})
    .sort_values(by="avg_runs", ascending=False)
)

print(toss_summary.head())

toss_summary.to_csv("output/toss_impact.csv", index=False)