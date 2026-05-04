import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

team_runs = (
    merged_df
    .groupby(["match_id", "batting_team"])["total_runs_calculated"]
    .sum()
    .reset_index()
    .rename(columns={"total_runs_calculated": "team_runs"})
    .sort_values(by=["match_id", "team_runs"], ascending=[True, False])
)

print(team_runs.head())

team_runs.to_csv("output/team_runs_per_match.csv", index=False)