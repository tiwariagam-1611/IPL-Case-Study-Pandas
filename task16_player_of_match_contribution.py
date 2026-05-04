import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

player_runs = (
    merged_df
    .groupby(["match_id", "batter"])["batsman_runs"]
    .sum()
    .reset_index()
)

max_runs = (
    player_runs
    .sort_values(["match_id", "batsman_runs"], ascending=[True, False])
    .drop_duplicates("match_id")
)

pom_data = merged_df[["match_id", "player_of_match"]].drop_duplicates()

comparison = max_runs.merge(
    pom_data,
    left_on="match_id",
    right_on="match_id",
    how="left"
)

comparison["is_top_scorer"] = comparison["batter"] == comparison["player_of_match"]

print(comparison.head())

comparison.to_csv("output/player_of_match_contribution.csv", index=False)