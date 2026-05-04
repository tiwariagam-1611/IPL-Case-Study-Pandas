import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

season_runs = (
    merged_df
    .groupby("season")["total_runs_calculated"]
    .sum()
    .reset_index()
    .rename(columns={"total_runs_calculated": "total_runs"})
    .sort_values(by="season")
)

print(season_runs)

season_runs.to_csv("output/season_trends.csv", index=False)