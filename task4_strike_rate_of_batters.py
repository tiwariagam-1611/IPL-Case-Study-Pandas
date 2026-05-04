import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

batter_stats = (
    merged_df
    .groupby("batter")
    .agg(
        runs=("batsman_runs", "sum"),
        balls=("ball", "count")
    )
    .reset_index()
)

batter_stats["strike_rate"] = (batter_stats["runs"] / batter_stats["balls"]) * 100

batter_stats = batter_stats.sort_values(by="strike_rate", ascending=False)

print(batter_stats.head())

batter_stats.to_csv("output/strike_rate.csv", index=False)