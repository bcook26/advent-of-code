# Day 2 Part 1 solution

with open("input2.txt","r") as f: 
    strat_guide = f.readlines()

total_score = 0

for round in strat_guide: 
    choices = round.strip()
    choices = round.split()
    
    computer_action, user_action = choices[0], choices[1]

    if user_action == "X":
        round_points = 1

        # round results
        if (computer_action == "A"):
            round_points += 3 
        elif (computer_action == "B"):
            round_points += 0
        elif (computer_action == "C"):
            round_points += 6

    #paper
    elif user_action == "Y":
        round_points = 2

        #round results 
        if computer_action == "A":
            round_points += 6
        elif computer_action == "B":
            round_points += 3
        elif computer_action == "C":
            round_points += 0

    elif user_action == "Z":
        round_points = 3

        if computer_action == "A": 
            round_points += 0 
        elif computer_action == "B":
            round_points += 6
        elif computer_action == "C":
            round_points += 3

    total_score += round_points
    print(total_score)