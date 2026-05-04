import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

team_runs = (
    merged_df
    .groupby(["match_id", "batting_team"])["total_runs_calculated"]
    .sum()
    .reset_index()
)

predicted_winner = (
    team_runs
    .sort_values(["match_id", "total_runs_calculated"], ascending=[True, False])
    .drop_duplicates("match_id")
    .rename(columns={"batting_team": "predicted_winner"})
)

actual_winner = (
    merged_df[["match_id", "winner"]]
    .drop_duplicates()
)

comparison = predicted_winner.merge(actual_winner, on="match_id")

comparison["correct_prediction"] = (
    comparison["predicted_winner"] == comparison["winner"]
)

accuracy = comparison["correct_prediction"].mean() * 100

print("Prediction Accuracy:", accuracy)

comparison.to_csv("output/winning_team_analysis.csv", index=False)