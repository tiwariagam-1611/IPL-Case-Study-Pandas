import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

powerplay = merged_df[merged_df["over"] <= 6]

powerplay_runs = (
    powerplay
    .groupby("batting_team")["total_runs_calculated"]
    .sum()
    .reset_index()
    .rename(columns={"total_runs_calculated": "powerplay_runs"})
    .sort_values(by="powerplay_runs", ascending=False)
)

print(powerplay_runs.head())

powerplay_runs.to_csv("output/powerplay_performance.csv", index=False)