import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

total_runs = (
    merged_df
    .groupby("batter")["batsman_runs"]
    .sum()
    .reset_index()
)

boundary_runs = (
    merged_df[merged_df["batsman_runs"].isin([4, 6])]
    .groupby("batter")["batsman_runs"]
    .sum()
    .reset_index()
    .rename(columns={"batsman_runs": "boundary_runs"})
)

boundary_percentage = total_runs.merge(boundary_runs, on="batter", how="left")

boundary_percentage["boundary_runs"] = boundary_percentage["boundary_runs"].fillna(0)

boundary_percentage["boundary_percentage"] = (
    boundary_percentage["boundary_runs"] / boundary_percentage["batsman_runs"]
) * 100

boundary_percentage = boundary_percentage.sort_values(by="boundary_percentage", ascending=False)

print(boundary_percentage.head())

boundary_percentage.to_csv("output/boundary_percentage.csv", index=False)