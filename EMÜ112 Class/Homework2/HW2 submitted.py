#   EMÜ 112 - Homework #2: COVID'19 Spread
#
#                                       SUMMARY
#   a)  On which day will more than half the population be infected (= Day Z) ?
#       - 1 person gets infected on day 1.
#       - Each infection lasts between 14-28 days (w. equal prob) & the person is infectious,
#           but after that period ends, they're no longer infectious & are also immune.
#       - Each person interacts w. a random number of others (between 0-10, w. equal prob)
#           every day (each person randomly selected, w. equal prob).
#       - The prob of infecting another person is 5%.
#
#   b)  Calculate how many ppl will be infected on Day Z.
#       Social distancing begins on day 20. Prob of one person interacting with n number of ppl:
#
#           n interactions:     0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10
#           probabilities:     50% | 25% | 10% |  5% |  3% |  2% |  1% |  1% |  1% |  1% |  1%

import random

def num_interacted_a():
    x = random.randint(0,10)          # function to generate a random number of interactions
    return(x)                         # (for the first 20 days and for part a)

def prob_infecting():
    x = random.randint(0, 100)        # function to see if someone gets infected
    if x <= 5:                        # 5 out of 100 chance
        return(True)

#def :

def sick_time():
    x = random.randint(14,28)         # function to generate a random number of sick days
    return(x)


population = 54450                                 # for testing
#population = 5445000                           # for the final result
print("\n\t   Calculating for a population of",population,"people")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

initial_pop = (0,)*population                   # create tuple to use in (a) and (b) --- maybe not needed?
infected = list(initial_pop)                    # status 0 indicates not being infected
immune = list(initial_pop)                      # list of ppl who will become immune / not reinfected
sick_days = list(initial_pop)                   # list with how many sick days are left

patient_zero=random.randint(0,(population-1))   # randomly select patient zero's index
#print(patient_zero)
infected[patient_zero] = 1                     # change their status to non-zero (infected)
immune[patient_zero] = 1                       # change their status to 1 (can't be reinfected)
sick_days[patient_zero] = sick_time()
day_count = 2
#print("~~~~~~~ Day 1 --> Infected:",infected,"-- will be immune: ",immune,"-- after this many days: ",sick_days)


while day_count < 20:                                    ######### change it to 20
    #print("\n~~~~~~~ Day",day_count)
    infected_today = list(initial_pop)
    for n in range(0,population):                       # for each infected person
        if infected[n] == 1:
            num_interacted = num_interacted_a()         # generate random number of their interactions
            list_interacted = [0]*num_interacted        # and make list with that many people
            did_they_interact = True
            interacted = 0                              # counter
            while interacted < len(list_interacted):    # find out how many of them will catch the virus
                caught_it = prob_infecting()
                if caught_it:
                    list_interacted[interacted] = 1    # mark them as infected (status = 1) in the interaction list
                interacted += 1
            #print("Person with index",n,"interacted with",num_interacted,"people.\tThose infected among them are:",list_interacted)

            interacted = 0                                  # counter
            list_index_interacted = [0]*num_interacted      # index numbers of the ppl which the infected person interacts with

            if num_interacted > 0:
                persons_index = random.randint(0, population-1)         # randomly select the first interacted person's index
                while n == persons_index:
                    persons_index = random.randint(0, population - 1)
                list_index_interacted[interacted] = persons_index  # and add to list of indexes
                interacted += 1
                #print("ppl's indexes:",persons_index,end=", ")

                while interacted < len(list_interacted):
                    while persons_index in list_index_interacted or n == persons_index:           # change the repeating indexes
                        persons_index = random.randint(0, population-1)
                    list_index_interacted[interacted] = persons_index  # add their index to the list of interacted
                    #print(persons_index, end=", ")
                    interacted += 1
                #print("Total interactions index list:", list_index_interacted,"\n")
            else:
                list_index_interacted = []         # make an empty list if they didn't interact
                did_they_interact = False

            #print(list_interacted)     # shows the people interacted with and whether they're infected(=1) or not(=0)
            #print(list_index_interacted)
            j = 0
            if did_they_interact:
                while j < num_interacted:  # adding features for infected:
                    #print("list:",list_index_interacted,"|| int numbers:",num_interacted,end="")
                    #print("|| j:",j,"|| infected's index:",list_index_interacted[j])
                    if list_interacted[j] == 1 and infected_today[list_index_interacted[j]] == 0 and infected[list_index_interacted[j]] == 0 and immune[list_index_interacted[j]] == 0:
                        infected_today[list_index_interacted[j]] += 1           # add to "infected today" list
                        immune[list_index_interacted[j]] += 1                   # add to "immune/can't be reinfected" list
                        sick_days[list_index_interacted[j]] += sick_time()      # generate random number of sick days
                    j += 1
            #print("population newly infected:",infected_today,"\twill be immune",immune,"after so many days:",sick_days)

    for m in range(0, population):
        if sick_days[m] > 0:
            sick_days[m] -= 1
        if infected_today[m] == 1:
            infected[m] += 1
    #print("end of day - pop infected:",infected_today,"\twill be immune", immune, "after so many days:", sick_days)
    day_count += 1

#print("\nlist of all infected ppl:",infected)

infected_count = 0
for x in range(population):
    if infected[x] == 1:
        infected_count += 1

print("\nTotal infected people until day 20:  ",infected_count,)

total_infected_until_day20 = tuple(infected)


########   Part (a)


infected_part_a = list(total_infected_until_day20)
Day_Z = False

while Day_Z == False:
    #print("\n~~~~~~~ Day", day_count)
    infected_today = list(initial_pop)
    for n in range(0, population):              # for each infected person
        if infected_part_a[n] == 1:
            num_interacted = num_interacted_a()  # generate random number of their interactions
            list_interacted = [0] * num_interacted  # and make list with that many people
            did_they_interact = True
            interacted = 0  # counter
            while interacted < len(list_interacted):  # find out how many of them will catch the virus
                caught_it = prob_infecting()
                if caught_it:
                    list_interacted[interacted] = 1  # mark them as infected (status = 1) in the interaction list
                interacted += 1
            #print("Person with index", n, "interacted with", num_interacted, "people.\tThose infected among them are:",list_interacted)

            interacted = 0  # counter
            list_index_interacted = [0] * num_interacted  # index numbers of the ppl which the infected person interacts with

            if num_interacted > 0:
                persons_index = random.randint(0, population - 1)  # randomly select the first interacted person's index
                while n == persons_index:
                    persons_index = random.randint(0, population - 1)
                list_index_interacted[interacted] = persons_index  # and add to list of indexes
                interacted += 1
                # print("ppl's indexes:",persons_index,end=", ")

                while interacted < len(list_interacted):
                    while persons_index in list_index_interacted or n == persons_index:  # change the repeating indexes
                        persons_index = random.randint(0, population - 1)
                    list_index_interacted[interacted] = persons_index  # add their index to the list of interacted
                    # print(persons_index, end=", ")
                    interacted += 1
                #print("Total interactions index list:", list_index_interacted, "\n")
            else:
                list_index_interacted = []  # make an empty list if they didn't interact
                did_they_interact = False

            # print(list_interacted)     # shows the people interacted with and whether they're infected(=1) or not(=0)
            # print(list_index_interacted)
            j = 0
            if did_they_interact:
                while j < num_interacted:  # adding features for infected:
                    # print("list:",list_index_interacted,"|| int numbers:",num_interacted,end="")
                    # print("|| j:",j,"|| infected's index:",list_index_interacted[j])
                    if list_interacted[j] == 1 and infected_today[list_index_interacted[j]] == 0 and infected_part_a[list_index_interacted[j]] == 0 and immune[list_index_interacted[j]] == 0:
                        infected_today[list_index_interacted[j]] += 1  # add to "infected today" list
                        immune[list_index_interacted[j]] += 1  # add to "immune/can't be reinfected" list
                        sick_days[list_index_interacted[j]] += sick_time()  # generate random number of sick days
                    j += 1
            #print("population newly infected:", infected_today, "\twill be immune", immune, "after so many days:",sick_days)

    for m in range(0, population):
        if sick_days[m] > 0:
            sick_days[m] -= 1
        if infected_today[m] == 1:
            infected_part_a[m] += 1
    #print("end of day - pop infected:", infected_today, "\twill be immune", immune, "after so many days:", sick_days)

    infected_count = 0
    for x in range(population):
        if infected_part_a[x] == 1:
            infected_count += 1

    if infected_count > int(population/2):
        Day_Z = True
    else:
        day_count += 1

Day_numbers = day_count

num_infected_part_a = infected_count
print("\nDay on which half of the population (",num_infected_part_a,") gets infected in part a:  ",day_count)


########   Part (b)

day_count = 20
infected_part_b = list(total_infected_until_day20)

def num_interacted_b():
    x = random.randint(0, 100)      # function to see how many people they interact with when there is social dist.
    if x <= 50:
        return (0)
    elif x > 50 and x <= 75:
        return (1)
    elif x > 70 and x <= 85:
        return (2)
    elif x > 85 and x <= 90:
        return (3)
    elif x > 90 and x <= 93:
        return (4)
    elif x > 93 and x <= 95:
        return (5)
    elif x == 96:
        return (6)
    elif x == 97:
        return (7)
    elif x == 98:
        return (8)
    elif x == 99:
        return (9)
    else:
        return (10)

while day_count <= Day_numbers:
    #print("\n~~~~~~~ Day", day_count)
    infected_today = list(initial_pop)
    for n in range(0, population):  # for each infected person
        if infected_part_b[n] == 1:
            num_interacted = num_interacted_b()  # generate random number of their interactions
            list_interacted = [0] * num_interacted  # and make list with that many people
            did_they_interact = True
            interacted = 0  # counter
            while interacted < len(list_interacted):  # find out how many of them will catch the virus
                caught_it = prob_infecting()
                if caught_it:
                    list_interacted[interacted] = 1  # mark them as infected (status = 1) in the interaction list
                interacted += 1
            #print("Person with index", n, "interacted with", num_interacted, "people.\tThose infected among them are:",list_interacted)

            interacted = 0  # counter
            list_index_interacted = [0] * num_interacted  # index numbers of the ppl which the infected person interacts with

            if num_interacted > 0:
                persons_index = random.randint(0, population - 1)  # randomly select the first interacted person's index
                while n == persons_index:
                    persons_index = random.randint(0, population - 1)
                list_index_interacted[interacted] = persons_index  # and add to list of indexes
                interacted += 1
                # print("ppl's indexes:",persons_index,end=", ")

                while interacted < len(list_interacted):
                    while persons_index in list_index_interacted or n == persons_index:  # change the repeating indexes
                        persons_index = random.randint(0, population - 1)
                    list_index_interacted[interacted] = persons_index  # add their index to the list of interacted
                    # print(persons_index, end=", ")
                    interacted += 1
                #print("Total interactions index list:", list_index_interacted, "\n")
            else:
                list_index_interacted = []  # make an empty list if they didn't interact
                did_they_interact = False

            # print(list_interacted)     # shows the people interacted with and whether they're infected(=1) or not(=0)
            # print(list_index_interacted)
            j = 0
            if did_they_interact:
                while j < num_interacted:  # adding features for infected:
                    # print("list:",list_index_interacted,"|| int numbers:",num_interacted,end="")
                    # print("|| j:",j,"|| infected's index:",list_index_interacted[j])
                    if list_interacted[j] == 1 and infected_today[list_index_interacted[j]] == 0 and infected_part_b[list_index_interacted[j]] == 0 and immune[list_index_interacted[j]] == 0:
                        infected_today[list_index_interacted[j]] += 1  # add to "infected today" list
                        immune[list_index_interacted[j]] += 1  # add to "immune/can't be reinfected" list
                        sick_days[list_index_interacted[j]] += sick_time()  # generate random number of sick days
                    j += 1
            #print("population newly infected:", infected_today, "\twill be immune", immune, "after so many days:",sick_days)

    for m in range(0, population):
        if sick_days[m] > 0:
            sick_days[m] -= 1
        if infected_today[m] == 1:
            infected_part_b[m] += 1
    #print("end of day - pop infected:", infected_today, "\twill be immune", immune, "after so many days:", sick_days)

    infected_count = 0
    for x in range(population):
        if infected_part_b[x] == 1:
            infected_count += 1

    day_count += 1

num_infected_part_b = infected_count
print("\nWith social distancing, instead of",num_infected_part_a,"people, only",num_infected_part_b,"people get infected")