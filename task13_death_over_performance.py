import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

death_overs = merged_df[merged_df["over"] >= 16]

death_runs = (
    death_overs
    .groupby("batting_team")["total_runs_calculated"]
    .sum()
    .reset_index()
    .rename(columns={"total_runs_calculated": "death_runs"})
    .sort_values(by="death_runs", ascending=False)
)

print(death_runs.head())

death_runs.to_csv("output/death_overs_performance.csv", index=False)