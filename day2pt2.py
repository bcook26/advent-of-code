# Day 2 Part 2 Solution: 
# X -> loss, Y -> draw, Z-> win

with open("input2.txt","r") as f: 
    strat_guide = f.readlines()

total_score = 0

for round in strat_guide: 
    choices = round.strip()
    choices = round.split()
    
    computer_action, outcome = choices[0], choices[1]

    round_points = 0


    if (outcome == "X"): # -> loss
        round_points = 0
        if (computer_action == "A"):
            round_points += 3

        elif (computer_action == "B"):
            round_points += 1

        elif computer_action == "C":
            round_points += 2
            
    elif (outcome == "Y"): # -> draw
        round_points = 3

        if (computer_action == "A"):
            round_points += 1 

        elif (computer_action == "B"):
            round_points += 2 

        elif computer_action == "C":
            round_points += 3

    elif (outcome == "Z"): # -> win
        round_points = 6

        if (computer_action == "A"):
            round_points += 2

        elif (computer_action == "B"):
            round_points += 3

        elif (computer_action == "C"):
            round_points += 1

    total_score += round_points
    print(total_score)
