# Cricket Tournament statistics
# Making a Dictionary of player and its tournament score
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}
#---------------------------------------------------------------------
# Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player, score in runs.items():
    if score > 500:
        print(player)
#-----------------------------------------------------------------------
# Orange Cap winner
orange_cap = max(runs, key=runs.get)
print("\nOrange Cap Winner:", orange_cap, "(", runs[orange_cap], ")", sep="")
#-------------------------------------------------------------------------
# Lowest scorer
lowest = min(runs, key=runs.get)
print("\nLowest Scorer:", lowest, "(", runs[lowest], ")", sep="")
#---------------------------------------------------------------------------
# Total runs scored
total_runs = sum(runs.values())
print("\nTotal Tournament Runs:", total_runs)
#---------------------------------------------------------------------------
# Players scoring below 400
below_400 = [player for player, score in runs.items() if score < 400]
print("\nPlayers Scoring Below 400:")
print(below_400)
#----------------------------------------------------------------------------
# Count players scoring between 400 and 600 runs
count = 0
for score in runs.values():
    if 400 <= score <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)