import pandas as pd

top_batters = pd.read_csv("../output/top_10_batters.csv")
economy = pd.read_csv("../output/top_10_bowlers_economy.csv")
death = pd.read_csv("../output/death_overs_performance.csv")
venue = pd.read_csv("../output/venue_analysis.csv")
season = pd.read_csv("../output/season_trends.csv")
consistency = pd.read_csv("../output/consistent_batters.csv")
powerplay = pd.read_csv("../output/powerplay_performance.csv")
boundary = pd.read_csv("../output/boundary_percentage.csv")
dot_balls = pd.read_csv("../output/dot_ball_analysis.csv")
runs_over = pd.read_csv("../output/runs_per_over.csv")

print("\n--- IPL DATA INSIGHTS ---\n")

b1 = consistency.iloc[0]
print(f"1. Most consistent batter is {b1['batter']} with average runs of {round(b1['avg_runs'],2)} across {int(b1['matches'])} matches.")

b2 = top_batters.iloc[0]
print(f"2. Highest run scorer is {b2['batter']} with {int(b2['total_runs'])} total runs.")

b3 = economy.iloc[0]
print(f"3. Most economical bowler is {b3['bowler']} with economy rate of {round(b3['economy'],2)}.")

b4 = death.iloc[0]
print(f"4. Best team in death overs is {b4['batting_team']} scoring {int(b4['death_runs'])} runs.")

b5 = powerplay.iloc[0]
print(f"5. Best powerplay team is {b5['batting_team']} with {int(b5['powerplay_runs'])} runs.")

b6 = venue.sort_values(by="avg_runs", ascending=False).iloc[0]
print(f"6. Highest scoring venue is {b6['venue']} with average runs of {round(b6['avg_runs'],2)}.")

b7 = boundary.iloc[0]
print(f"7. Batter with highest boundary percentage is {b7['batter']} with {round(b7['boundary_percentage'],2)}% of runs from boundaries.")

b8 = dot_balls.iloc[0]
print(f"8. Bowler with most dot balls is {b8['bowler']} with {int(b8['dot_balls'])} dot deliveries.")

b9 = runs_over.sort_values(by="avg_runs", ascending=False).iloc[0]
print(f"9. Highest scoring over is over {int(b9['over'])} with average runs of {round(b9['avg_runs'],2)}.")

b10 = season.iloc[-1]
print(f"10. Latest season ({b10['season']}) recorded total runs of {int(b10['total_runs'])}, showing overall scoring trends.")