import regex as re
import numpy as np

# Dictionary
cubes = ["red", "green", "blue"]
# Define Ruleset
cubeCount = [12 , 13, 14]

i = 0
total = 0
for line in open("./input"):
    x = re.findall("(\d blue|\d red|\d green|;|\d\d blue|\d\d green|\d\d red)", line)

    score = 0
    for item in x:
        if item != ";":
            temp = item.split(" ")
            # print(temp)
            for cube in cubes:
                if temp[1] == cube:
                    if int(temp[0]) > cubeCount[cubes.index(cube)]:
                        score += 1
    i += 1
    if score == 0:
        total = int(i) + total
        print(i)
    else:
        print("Game " + str(i) + " is invalid")
print(total)