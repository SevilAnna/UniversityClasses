#   EMÜ 112 - Homework #1: Shooter Simulation

import random

# counting how many times they win in each situation
A_counter = 0
B_counter = 0
C_counter = 0
A_counter2 = 0
B_counter2 = 0
C_counter2 = 0

n = int(input("How many times shall the simulation run?  "))
print("Calculating...")

for i in range (0,n,1):

# determining the order they'll shoot:
    orderA = random.randint(1,3)
    orderB = random.randint(1,3)
    while orderA == orderB:
        orderB = random.randint(1,3)
    orderC = random.randint(1,3)
    while orderA == orderC or orderB == orderC:
        orderC = random.randint(1,3)
#    print("The order is:", end="")
#    print("   A:", orderA, " ,  B:", orderB, " ,  C:", orderC, end="    -->   ")
# status (True = alive, False = dead)
    statusA = True
    statusB = True
    statusC = True

# chances of living when C shoots upwards (in the air) should be:
#   A : 30%
#   B : 18%
#   C : 52%

    #   when A gets to shoot first
    if orderA == 1:                                             # A shoots B (100% chance)
        statusB = False                                         # B dies
        chance = random.randint(0, 100)
        if chance <= 50:                                        # C shoots at A (50% chance)
           statusA = False                                      # if A dies
           winner = 3                                           # C wins
        else:                                                   # otherwise A shoots C (100% chance)
            statusC = False                                     # C dies
            winner = 1                                          # and A wins

    #   when B gets to shoot first
    elif orderB == 1:
        chance = random.randint(0, 100)
        if chance <= 80:                                        # B shoots at A (80% chance)
            statusA = False                                     # if A dies
            while statusB == True and statusC == True:          # while B and C are both still alive
                chance = random.randint(0, 100)
                if chance <= 50:                                # C shoots at B (50% chance)
                    statusB = False                             # if B dies
                    winner = 3                                  # C wins
                else:                                           # otherwise
                    chance = random.randint(0, 100)
                    if chance <= 80:                            # B shoots at C (80% chance)
                        statusC = False                         # if C dies
                        winner = 2                              # B wins. repeat if neither B nor C hits their target.
        else:                                                   # otherwise (if B misses A)
            if orderA == 2:                                     # if A goes second, A shoots B (100% chance)
                statusB = False                                 # B dies
                chance = random.randint(0, 100)
                if chance <= 50:                                # C shoots at A (50% chance)
                    statusA = False                             # if A dies
                    winner = 3                                  # C wins.
                else:                                           # otherwise A shoots C (100% chance)
                    statusC = False                             # C dies
                    winner = 1                                  # A wins.
            else:                                               # if C goes second, C shoots up, A shoots B (100% chance)
                statusB = False                                 # B dies.
                chance = random.randint(0, 100)
                if chance <= 50:                                # C shoots at A (50% chance)
                    statusA = False                             # if A dies
                    winner = 3                                  # C wins
                else:                                           # otherwise A shoots C (100% chance)
                    statusC = False                             # C dies
                    winner = 1                                  # A wins.

    #   if C gets to shoot first
    elif orderC == 1:                                           # C shoots up
        if orderA == 2:                                         # if A goes second, A shoots B (100% chance)
            statusB = False                                     # B dies.
            chance = random.randint(0, 100)
            if chance <= 50:                                    # C shoots at A (50% chance)
                statusA = False                                 # if A dies
                winner = 3                                      # C wins
            else:                                               # otherwise A shoots C (100% chance)
                statusC = False                                 # C dies
                winner = 1                                      # A wins.
        else:                                                   # if B goes second
            chance = random.randint(0, 100)
            if chance <= 80:                                    # B shoots at A (80% chance)
                statusA = False                                 # A dies.
                while statusB == True and statusC == True:      # while B and C are both still alive
                    chance = random.randint(0, 100)
                    if chance <= 50:                            # C shoots at B (50% chance)
                        statusB = False                         # if B dies
                        winner = 3                              # C wins
                    else:                                       # otherwise
                        chance = random.randint(0, 100)
                        if chance <= 80:                        # B shoots at C (80% chance)
                            statusC = False                     # if C dies
                            winner = 2                          # B wins. repeat if neither B nor C hits their target.
            else:                                               # if B misses A, A shoots B (100% chance)
                statusB = False                                 # B dies
                chance = random.randint(0, 100)
                if chance <= 50:                                # C shoots at A (50% chance)
                    statusA = False                             # if A dies
                    winner = 3                                  # C wins
                else:                                           # otherwise A shoots C (100% chance)
                    statusC = False                             # C dies
                    winner = 1                                  # A wins.
    if statusA == True:
#        print("A wins")
        A_counter += 1
    if statusB == True:
#        print("B wins")
        B_counter += 1
    if statusC == True:
#        print("C wins")
        C_counter += 1



#################################################################################################


    statusA = True
    statusB = True
    statusC = True

# when C doesn't shoot up
    #   when A gets to shoot first
    if orderA == 1:                                             # A shoots B (100% chance)
        statusB = False                                         # B dies
        chance = random.randint(0, 100)
        if chance <= 50:                                        # C shoots at A (50% chance)
           statusA = False                                      # if A dies
           winner = 3                                           # C wins
        else:                                                   # otherwise A shoots C (100% chance)
            statusC = False                                     # C dies
            winner = 1                                          # and A wins

    #   when B gets to shoot first
    elif orderB == 1:
        chance = random.randint(0, 100)
        if chance <= 80:                                        # B shoots at A (80% chance)
            statusA = False                                     # if A dies
            while statusB == True and statusC == True:          # while B and C are both still alive
                chance = random.randint(0, 100)
                if chance <= 50:                                # C shoots at B (50% chance)
                    statusB = False                             # if B dies
                    winner = 3                                  # C wins
                else:                                           # otherwise
                    chance = random.randint(0, 100)
                    if chance <= 80:                            # B shoots at C (80% chance)
                        statusC = False                         # if C dies
                        winner = 2                              # B wins. repeat if neither B nor C hits their target.
        else:                                                   # otherwise (if B misses A)
            if orderA == 2:                                         # if A goes second, A shoots B (100% chance)
                statusB = False                                     # B dies
                chance = random.randint(0, 100)
                if chance <= 50:                                    # C shoots at A (50% chance)
                    statusA = False                                 # if A dies
                    winner = 3                                      # C wins.
                else:                                               # otherwise A shoots C (100% chance)
                    statusC = False                                 # C dies
                    winner = 1                                      # A wins.
            else:                                                   # if C goes second
                chance = random.randint(0, 100)
                if chance <= 50:                                    # C shoots at A (50% chance)
                    statusA = False                                 # if A dies
                    while statusB == True and statusC == True:      # while B and C are both still alive
                        chance = random.randint(0, 100)
                        if chance <= 80:                            # B shoots at C
                            statusC = False                         # if C dies
                            winner = 2                              # B wins
                        else:
                            chance = random.randint(0, 100)
                            if chance <= 50:                        # C shoots at B
                                statusB = False                     # if B dies
                                winner = 3                          # C wins
                else:                                       # if C misses A
                    statusB = False                         # A shoots B (100% chance)
                    chance = random.randint(0, 100)
                    if chance <= 50:                        # C shoots at A (50% chance)
                        statusA = False                     # if A dies 
                        winner = 3                          # C wins
                    else:                                   # otherwise A shoots C (100% chance)
                        statusC = False                     # C dies
                        winner = 1                          # A wins
                    
                            
    #   if C gets to shoot first
    elif orderC == 1:
        chance = random.randint(0, 100)
        if chance <= 50:                                        # C shoots at A (50% chance)
                statusA = False                                 # if A dies
                while statusB == True and statusC == True:      # when B and C are both alive
                    chance = random.randint(0, 100)
                    if chance <= 80:                            # B shoots at C (80% chance)
                        statusC = False                         # if C dies
                        winner = 2                              # B wins
                    else:                                       # if B misses C
                        chance = random.randint(0, 100)
                        if chance <= 50:                        # C shoots at B (%50 chance)
                            statusB = False                     # if B dies
                            winner = 3                          # C wins. repeat if neither B nor C hits their target.
        else:                                                   # if C misses A
            if orderA == 2:                                     # if A goes second, A shoots at B (100% chance)
                statusB = False                                 # B dies.
                chance = random.randint(0, 100)
                if chance <= 50:                                # C shoots at A (50% chance)
                    statusA = False                             # if A dies
                    winner = 3                                  # C wins
                else:                                           # otherwise A shoots C (100% chance)
                    statusC = False                             # C dies
                    winner = 1                                  # A wins.

            else:                                              # if B goes second
                chance = random.randint(0, 100)
                if chance <= 80:                                # B shoots at A (80% chance)
                    statusA = False                             # if A dies
                    while statusB == True and statusC == True:  # while B and C are both still alive
                        chance = random.randint(0, 100)
                        if chance <= 50:                        # C shoots at B (50% chance)
                            statusB = False                     # if B dies
                            winner = 3                          # C wins
                        else:                                   # otherwise
                            chance = random.randint(0, 100)
                            if chance <= 80:                    # B shoots at C (80% chance)
                                statusC = False                 # if C dies
                                winner = 2                      # B wins. repeat if neither B nor C hits their target.
                else:                                           # if B misses A, A shoots B (100% chance)
                    statusB = False                             # B dies
                    chance = random.randint(0, 100)
                    if chance <= 50:                            # C shoots at A (50% chance)
                        statusA = False                         # if A dies
                        winner = 3                              # C wins
                    else:                                       # otherwise A shoots C (100% chance)
                        statusC = False                         # C dies
                        winner = 1                              # A wins.

    if statusA == True:
#        print("A wins")
        A_counter2 += 1
    if statusB == True:
#        print("B wins")
        B_counter2 += 1
    if statusC == True:
#        print("C wins")
        C_counter2 += 1


A_percentage = A_counter / n *100
B_percentage = B_counter / n *100
C_percentage = C_counter / n *100
print("\nChances of them surviving when Can shoots in the air in round 1 are:")
print("   A: ", A_percentage,"%,  B: ", B_percentage,"%,  C:",C_percentage,"%")

A_percentage2 = A_counter2 / n *100
B_percentage2 = B_counter2 / n *100
C_percentage2 = C_counter2 / n *100
print("\nChances of them surviving when Can shoots someone in round 1 are:")
print("   A: ", A_percentage2,"%,  B: ", B_percentage2,"%,  C:",C_percentage2,"%")
