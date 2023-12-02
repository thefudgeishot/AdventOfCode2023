import regex as re
import numpy as np

# numbers
numberT = ["one","two","three","four","five","six","seven","eight","nine"]
numberD = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0
for line in open("./input"):
    # filter text
    x = re.findall("([^a-z]|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True)
    #print(x)

    # sanitise array
    array = []
    for item in x:
        if str(item) in numberT:
            print(str(item))
            i = 0
            for number in numberT:
                if str(item) == str(number):
                    # append to new array
                    print(str(numberD[i]))
                    array.append(str(numberD[i]))
                i += 1
        elif item != "\n":
            array.append(item)
        
    digit = str(array[0]) + str(array[-1])
    #print(array)
    #print("digit = " + digit)
    total = int(digit) + int(total)

print(total)
    