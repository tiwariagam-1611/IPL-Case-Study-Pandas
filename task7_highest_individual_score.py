import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

batter_match_runs = (
    merged_df
    .groupby(["match_id", "batter"])["batsman_runs"]
    .sum()
    .reset_index()
)

highest_score = (
    batter_match_runs
    .sort_values(by="batsman_runs", ascending=False)
    .head(1)
)

print(highest_score)

highest_score.to_csv("output/highest_individual_score.csv", index=False)