import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

bowler_stats = (
    merged_df
    .groupby("bowler")
    .agg(
        runs_conceded=("total_runs_calculated", "sum"),
        balls=("ball", "count")
    )
    .reset_index()
)

bowler_stats["overs"] = bowler_stats["balls"] / 6
bowler_stats["economy"] = bowler_stats["runs_conceded"] / bowler_stats["overs"]

top_bowlers = bowler_stats.sort_values(by="economy").head(10)

print(top_bowlers)

top_bowlers.to_csv("output/top_10_bowlers_economy.csv", index=False)