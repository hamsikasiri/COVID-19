import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Datasets
# -----------------------------
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

sns.set_style("whitegrid")

print("Matches Dataset Shape:", matches.shape)
print("Deliveries Dataset Shape:", deliveries.shape)

# -----------------------------
# Most Winning Teams
# -----------------------------
wins = matches['winner'].value_counts()

print("\nTop 10 Winning Teams:")
print(wins.head(10))

plt.figure(figsize=(10, 6))
sns.barplot(
    x=wins.head(10).index,
    y=wins.head(10).values
)
plt.title("Top 10 IPL Teams by Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Top Run Scorers
# -----------------------------
top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum()
top_batsmen = top_batsmen.sort_values(
    ascending=False
).head(10)

print("\nTop 10 Run Scorers:")
print(top_batsmen)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_batsmen.index,
    y=top_batsmen.values
)
plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Top Stadiums
# -----------------------------
stadiums = matches['venue'].value_counts().head(10)

print("\nTop Stadiums:")
print(stadiums)

plt.figure(figsize=(12, 6))
sns.barplot(
    x=stadiums.index,
    y=stadiums.values
)
plt.title("Top 10 Stadiums by Matches Hosted")
plt.xlabel("Stadium")
plt.ylabel("Matches Hosted")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# -----------------------------
# Toss Winner vs Match Winner
# -----------------------------
toss_match = matches[
    matches['toss_winner'] == matches['winner']
]

percentage = (len(toss_match) / len(matches)) * 100

print(
    f"\nToss Winner also Won Match: {percentage:.2f}%"
)

# -----------------------------
# Top Player of the Match Awards
# -----------------------------
pom = matches['player_of_match'].value_counts().head(10)

print("\nTop Player of the Match Award Winners:")
print(pom)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=pom.index,
    y=pom.values
)
plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Players")
plt.ylabel("Awards")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Top Wicket Takers
# -----------------------------
wickets = deliveries[
    deliveries['player_dismissed'].notna()
]

top_bowlers = wickets['bowler'].value_counts().head(10)

print("\nTop 10 Wicket Takers:")
print(top_bowlers)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_bowlers.index,
    y=top_bowlers.values
)
plt.title("Top 10 IPL Wicket Takers")
plt.xlabel("Bowlers")
plt.ylabel("Wickets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Matches Per Season
# -----------------------------
if 'season' in matches.columns:

    season_matches = (
        matches['season']
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        x=season_matches.index,
        y=season_matches.values,
        marker='o'
    )

    plt.title("IPL Matches Per Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.tight_layout()
    plt.show()

print("\nIPL EDA Analysis Completed Successfully!")