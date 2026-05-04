import pandas as pd

merged_df = pd.read_csv("merged_data.csv", low_memory=False)

venue_matches = (
    merged_df[["match_id", "venue"]]
    .drop_duplicates()
    .groupby("venue")
    .count()
    .reset_index()
    .rename(columns={"match_id": "total_matches"})
)

venue_runs = (
    merged_df
    .groupby("venue")["total_runs_calculated"]
    .mean()
    .reset_index()
    .rename(columns={"total_runs_calculated": "avg_runs"})
)

venue_analysis = venue_matches.merge(venue_runs, on="venue")

print(venue_analysis.head())

venue_analysis.to_csv("output/venue_analysis.csv", index=False)