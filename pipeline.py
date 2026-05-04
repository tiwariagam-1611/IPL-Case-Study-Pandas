import pandas as pd

deliveries_file = "deliveries.csv"
matches_file = "matches.csv"

deliveries_df = pd.read_csv(deliveries_file)
matches_df = pd.read_csv(matches_file)

print("Loaded Successfully")
print("Deliveries Shape:", deliveries_df.shape)
print("Matches Shape:", matches_df.shape)

print("\nMissing Values:\n", deliveries_df.isnull().sum())
print("\nMissing Values:\n", matches_df.isnull().sum())

num_cols = deliveries_df.select_dtypes(include=['number']).columns
deliveries_df[num_cols] = deliveries_df[num_cols].fillna(0)

cat_cols = deliveries_df.select_dtypes(include=['object', 'string']).columns
deliveries_df[cat_cols] = deliveries_df[cat_cols].fillna("NA")

matches_df['winner'] = matches_df['winner'].fillna("No Result")
matches_df['method'] = matches_df['method'].fillna("Regular")
print(matches_df.head())
# matches_df = matches_df.fillna("NA")

deliveries_df['match_id'] = deliveries_df['match_id'].astype(int)
matches_df['id'] = matches_df['id'].astype(int)

print("\nID Check:")
print("Deliveries IDs:", deliveries_df['match_id'].nunique())
print("Matches IDs:", matches_df['id'].nunique())

deliveries_df['total_runs_calculated'] = (
    deliveries_df['batsman_runs'] + deliveries_df['extra_runs']
)

deliveries_df.columns = deliveries_df.columns.str.lower().str.replace(" ", "_")
matches_df.columns = matches_df.columns.str.lower().str.replace(" ", "_")

merged_df = deliveries_df.merge(
    matches_df,
    left_on="match_id",
    right_on="id",
    how="inner"
)

merged_df.to_csv("merged_data.csv", index=False)

print("\nMerged Shape:", merged_df.shape)
print("Done")