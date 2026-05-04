import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

top_batters = (
    merged_df
    .groupby("batter")["batsman_runs"]
    .sum()
    .reset_index()
    .rename(columns={"batsman_runs": "total_runs"})
    .sort_values(by="total_runs", ascending=False)
    .head(10)
)

print(top_batters)

top_batters.to_csv("output/top_10_batters.csv", index=False)