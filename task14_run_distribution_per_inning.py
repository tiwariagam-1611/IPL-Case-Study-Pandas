import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

inning_runs = (
    merged_df
    .groupby("inning")["total_runs_calculated"]
    .sum()
    .reset_index()
    .rename(columns={"total_runs_calculated": "total_runs"})
)

print(inning_runs)

inning_runs.to_csv("output/run_distribution_inning.csv", index=False)