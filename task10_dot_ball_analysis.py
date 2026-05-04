import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

dot_balls = merged_df[merged_df["total_runs_calculated"] == 0]

dot_ball_count = (
    dot_balls
    .groupby("bowler")["ball"]
    .count()
    .reset_index()
    .rename(columns={"ball": "dot_balls"})
    .sort_values(by="dot_balls", ascending=False)
)

print(dot_ball_count.head())

dot_ball_count.to_csv("output/dot_ball_analysis.csv", index=False)