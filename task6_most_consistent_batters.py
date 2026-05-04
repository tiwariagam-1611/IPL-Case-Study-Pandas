import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

batter_match_runs = (
    merged_df
    .groupby(["batter", "match_id"])["batsman_runs"]
    .sum()
    .reset_index()
)

consistency = (
    batter_match_runs
    .groupby("batter")
    .agg(
        avg_runs=("batsman_runs", "mean"),
        matches=("match_id", "nunique")
    )
    .reset_index()
)

consistent_batters = (
    consistency[consistency["matches"] >= 20]
    .sort_values(by="avg_runs", ascending=False)
    .head(10)
)

print(consistent_batters)

consistent_batters.to_csv("output/consistent_batters.csv", index=False)