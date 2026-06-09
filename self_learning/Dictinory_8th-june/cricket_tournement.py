players = {
"Virat":{"runs":645,"matches":12,"wickets":0},
"Rohit":{"runs":512,"matches":12,"wickets":1},
"Gill":{"runs":698,"matches":12,"wickets":0},
"Rahul":{"runs":435,"matches":11,"wickets":0},
"Hardik":{"runs":278,"matches":10,"wickets":8},
"Pant":{"runs":534,"matches":12,"wickets":0},
"Surya":{"runs":389,"matches":11,"wickets":1},
"Jadeja":{"runs":301,"matches":12,"wickets":12},
"Ashwin":{"runs":210,"matches":10,"wickets":15},
"Shami":{"runs":55,"matches":12,"wickets":22},
"Bumrah":{"runs":40,"matches":11,"wickets":20},
"Siraj":{"runs":35,"matches":10,"wickets":18},
"Kuldeep":{"runs":80,"matches":12,"wickets":17},
"Axar":{"runs":250,"matches":11,"wickets":10},
"Ishan":{"runs":320,"matches":9,"wickets":0},
"Samson":{"runs":410,"matches":10,"wickets":0},
"Gaikwad":{"runs":560,"matches":12,"wickets":0},
"Tilak":{"runs":355,"matches":10,"wickets":1},
"Rinku":{"runs":330,"matches":9,"wickets":0},
"Chahal":{"runs":25,"matches":10,"wickets":16},
"Arshdeep":{"runs":20,"matches":11,"wickets":19},
"Avesh":{"runs":18,"matches":9,"wickets":11},
"Washington":{"runs":220,"matches":8,"wickets":9},
"Deepak":{"runs":75,"matches":7,"wickets":13},
"Prasidh":{"runs":15,"matches":8,"wickets":8},
"Abhishek":{"runs":470,"matches":11,"wickets":6},
"Nitish":{"runs":290,"matches":10,"wickets":7},
"Varun":{"runs":60,"matches":10,"wickets":14},
"Harshit":{"runs":30,"matches":8,"wickets":12},
"Mukesh":{"runs":22,"matches":7,"wickets":10}
}

# 1. Display all players
print("ALL PLAYER STATISTICS")
for p in players:
    print(p, players[p])

# 2,3,4,5
first = True
total_runs = 0
total_wickets = 0
count = 0

for p in players:

    runs = players[p]["runs"]
    wickets = players[p]["wickets"]

    total_runs = total_runs + runs
    total_wickets = total_wickets + wickets
    count = count + 1

    if first:
        highest = p
        lowest = p
        bestbowler = p

        maxruns = runs
        minruns = runs
        maxwickets = wickets

        first = False

    if runs > maxruns:
        maxruns = runs
        highest = p

    if runs < minruns:
        minruns = runs
        lowest = p

    if wickets > maxwickets:
        maxwickets = wickets
        bestbowler = p

average_runs = total_runs / count

print("\nHighest Run Scorer")
print(highest, players[highest])

print("\nLowest Run Scorer")
print(lowest, players[lowest])

print("\nAverage Runs =", average_runs)

print("\nMaximum Wickets")
print(bestbowler, players[bestbowler])

# 6. All Rounders
print("\nALL ROUNDERS")

for p in players:
    if players[p]["runs"] > 300 and players[p]["wickets"] > 5:
        print(p)

# 7. Above Average Players
print("\nABOVE AVERAGE BATSMEN")

for p in players:
    if players[p]["runs"] > average_runs:
        print(p, players[p]["runs"])

# 8. Categories
print("\nPLAYER CATEGORIES")

for p in players:

    runs = players[p]["runs"]

    if runs >= 500:
        category = "Star Performer"

    elif runs >= 300:
        category = "Good Performer"

    elif runs >= 150:
        category = "Average Performer"

    else:
        category = "Poor Performer"

    print(p, "-", category)

# 9. Team Statistics
print("\nTEAM STATISTICS")
print("Total Players =", count)
print("Total Runs =", total_runs)
print("Total Wickets =", total_wickets)
print("Average Runs =", average_runs)

# 10. Top 5 Batsmen
batsmen = []

for p in players:
    batsmen.append([players[p]["runs"], p])

batsmen.sort(reverse=True)

print("\nTOP 5 BATSMEN")

for i in range(5):
    print(batsmen[i][1], batsmen[i][0])

# 11. Top 5 Bowlers
bowlers = []

for p in players:
    bowlers.append([players[p]["wickets"], p])

bowlers.sort(reverse=True)

print("\nTOP 5 BOWLERS")

for i in range(5):
    print(bowlers[i][1], bowlers[i][0])

# 12. Award Winners
awards = {}

for p in players:

    if players[p]["runs"] >= 500 or players[p]["wickets"] >= 15:
        awards[p] = players[p]

print("\nAWARD WINNERS")

for p in awards:
    print(p, awards[p])

# Tournament Report
print("\n===== TOURNAMENT REPORT =====")
print("Highest Run Scorer =", highest)
print("Runs =", maxruns)

print("Best Bowler =", bestbowler)
print("Wickets =", maxwickets)

print("Average Runs =", average_runs)
print("Award Winners =", len(awards))
print("Total Runs Scored =", total_runs)
print("Total Wickets Taken =", total_wickets)