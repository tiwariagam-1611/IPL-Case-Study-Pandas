import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

boundaries = merged_df[merged_df["batsman_runs"].isin([4, 6])]

boundary_count = (
    boundaries
    .groupby("batter")["batsman_runs"]
    .count()
    .reset_index()
    .rename(columns={"batsman_runs": "boundary_count"})
    .sort_values(by="boundary_count", ascending=False)
)

print(boundary_count.head())

boundary_count.to_csv("output/boundary_analysis.csv", index=False)