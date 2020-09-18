#   EMÜ 112 - Homework #3: Triangle Counter


def strip_file_line(x):         # function for stripping "\n" and removing "-"
    x = x.rstrip("\n")
    x = list(x)
    while "-" in x:
        x.remove("-")
    return(x)


shape = open("triangles.txt", "r")
lines = []                                  # create list to store the lines in
line_check = shape.readline()
line = strip_file_line(line_check)          # read, strip & append first line to the list
lines.append(line)
while line_check != '':
    line_check = shape.readline()
    line = strip_file_line(line_check)
    lines.append(line)                      # repeat with other lines & append to the list
#print(len(lines),lines)
# for some reason the "lines" list's length is 11 instead of 10.

dict_lines = {}                             # create a dictionary that'll have all lines in it
keycounter = 0
for i in range(0, len(lines)-1):            # ("-1" is in order to fix the problem written in line 30)
    templist = []
    for j in range(0, len(lines[i])):
        templist.append(lines[i][j])
    dict_lines[keycounter] = templist       # add all lines to it
    keycounter += 1
#print(dict_lines)


all_letters = set()                         # create a set in order to get all unique letters
for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):        # add all letters to it
        all_letters.add(lines[i][j])
#print(all_letters)
letter_list = list(all_letters)             # create a list with all letters in it
#print(len(letter_list),letter_list)

letter_combos = []                          # create a list that'll have all letter combinations (w.o. duplicates)
for x in range(0,len(letter_list)):
    for y in range(0,len(letter_list)):
        for z in range(0, len(letter_list)):
            if x != y and x != z and y != z:
                temp1 = letter_list[x]+letter_list[y]+letter_list[z]    # 3! = 6 possible combinations for any x,y,z.
                temp2 = letter_list[x]+letter_list[z]+letter_list[y]        # This example should have a total of 120
                temp3 = letter_list[y]+letter_list[z]+letter_list[x]        # unique combinations: C(n,3) , here n=10.
                temp4 = letter_list[y]+letter_list[x]+letter_list[z]        # (n: number of letters - line 49)
                temp5 = letter_list[z]+letter_list[y]+letter_list[x]        # Check if C value is correct on line 67.
                temp6 = letter_list[z]+letter_list[x]+letter_list[y]                # For each unique combination
                if temp1 not in letter_combos and temp2 not in letter_combos:       # we need only one of the 6 comb.s
                    if temp3 not in letter_combos and temp4 not in letter_combos:   # created using the same x,y,z
                        if temp5 not in letter_combos and temp6 not in letter_combos:   # so we pick the first one:
                            letter_combos.append(temp1)         # If the found letter combo isn't in the list, add it
#print(len(letter_combos),letter_combos)

triangles = []                              # Find those that form triangles using letters from letter_combos. For
for i in range(0,len(letter_combos)):       # each line, 2 of those letters should be on the line, but not the 3rd one.
    sidecounter = 0                         # (ex: a,b on one line; b,c on another line; c,b on another line)
    for j in range(0,len(dict_lines)):      # sidecounter counts found sides of a triangle. += if above cond. fulfilled
        if letter_combos[i][0] in dict_lines[j] and letter_combos[i][1] in dict_lines[j]:
            if letter_combos[i][2] not in dict_lines[j]:
                sidecounter += 1
        if letter_combos[i][0] in dict_lines[j] and letter_combos[i][2] in dict_lines[j]:
            if letter_combos[i][1] not in dict_lines[j]:
                sidecounter += 1
        if letter_combos[i][2] in dict_lines[j] and letter_combos[i][1] in dict_lines[j]:
            if letter_combos[i][0] not in dict_lines[j]:
                sidecounter += 1
    if sidecounter == 3:                            # if a triangle is formed, add it to the triangles list
        triangles.append(letter_combos[i])
#print(triangles)
print("\n\tThere are",len(triangles),"triangles.")  # 59 lines of code to get the result, excluding comments etc. :)
