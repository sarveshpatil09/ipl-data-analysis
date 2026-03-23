import pandas as pd
import matplotlib.pyplot as plt

# IPL dataset
data = {
    "Team": [
        "CSK","MI","RCB","KKR","CSK","MI","RCB","KKR",
        "CSK","MI","RCB","KKR","CSK","MI","RCB","KKR"
    ],
    "Player": [
        "Dhoni","Rohit","Kohli","Russell",
        "Raina","Surya","Faf","Gill",
        "Jadeja","Pollard","Maxwell","Narine",
        "Bravo","Hardik","ABD","Iyer"
    ],
    "Runs": [
        45,60,75,50,
        30,65,55,40,
        35,48,62,33,
        25,70,85,44
    ],
    "Wickets": [
        0,0,0,2,
        0,0,0,1,
        2,1,0,3,
        2,0,0,0
    ],
    "Match_Result": [
        "Win","Win","Lose","Win",
        "Lose","Win","Lose","Win",
        "Win","Lose","Win","Win",
        "Lose","Win","Win","Lose"
    ]
}

df = pd.DataFrame(data)

print("IPL Dataset")
print(df)

# Team total runs
team_runs = df.groupby("Team")["Runs"].sum()
print("\nTotal Runs by Team")
print(team_runs)

# Team total wickets
team_wickets = df.groupby("Team")["Wickets"].sum()
print("\nTotal Wickets by Team")
print(team_wickets)

# Top run scorers
top_runs = df.sort_values(by="Runs", ascending=False).head(5)
print("\nTop Run Scorers")
print(top_runs)

# Top wicket takers
top_wickets = df.sort_values(by="Wickets", ascending=False).head(5)
print("\nTop Wicket Takers")
print(top_wickets)

# Team wins
wins = df[df["Match_Result"] == "Win"]
team_wins = wins.groupby("Team").size()

print("\nTeam Wins")
print(team_wins)

# Graphs
plt.figure()
team_runs.plot(kind="bar")
plt.title("Total Runs by Team")
plt.xlabel("Team")
plt.ylabel("Runs")
plt.show()

plt.figure()
team_wickets.plot(kind="bar")
plt.title("Total Wickets by Team")
plt.xlabel("Team")
plt.ylabel("Wickets")
plt.show()

plt.figure()
team_wins.plot(kind="bar")
plt.title("Match Wins by Team")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.show()

# Player performance
print("\nPlayer Performance Analysis")

for index,row in df.iterrows():

    score = row["Runs"] + (row["Wickets"]*20)

    if score > 80:
        level = "Excellent"
    elif score > 60:
        level = "Good"
    elif score > 40:
        level = "Average"
    else:
        level = "Poor"

    print(row["Player"],":",level)

# Save results
team_runs.to_csv("team_runs.csv")
team_wickets.to_csv("team_wickets.csv")

print("\nAnalysis files saved.")
