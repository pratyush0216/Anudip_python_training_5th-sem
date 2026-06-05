# program to take input of 11 player and show there score 
# PLAYER SCORE 
print("----------PLAYER---------")

player_score = []                 #create a list
# Take the input form user
for i in range(11):
    score = int(input("Input the score of player {} :" .format(i + 1) ))
    player_score.append(score)
print("\n-----------player score-----------")
print("score of player{} :", player_score) 

# To finding the higest score
max_score = player_score[0]
for index in range (1,len(player_score)):
    if player_score[index] > max_score:
        max_score = player_score[index]
print("The Higest score is : ",max_score)        
