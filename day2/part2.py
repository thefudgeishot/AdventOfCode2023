import regex as re
import numpy as np

# Dictionary
cubes = ["red", "green", "blue"]

i = 0
total = 0
for line in open("./input"):
    x = re.findall("(\d blue|\d red|\d green|;|\d\d blue|\d\d green|\d\d red)", line)

    # Define ruleset
    highest = [0, 0, 0]

    score = 0
    for item in x:
        if item != ";":
            temp = item.split(" ")
            # print(temp)
            for cube in cubes:
                if temp[1] == cube:
                    if int(temp[0]) > highest[cubes.index(cube)]:
                        highest[cubes.index(cube)] = int(temp[0])
    total = (int(highest[0]) * int(highest[1]) * int(highest[2])) + total
print(total)