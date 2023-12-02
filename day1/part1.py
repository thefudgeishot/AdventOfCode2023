import regex as re

total = 0
for line in open("./input"):
    x = re.findall("[^a-z]", line)
    digit = str(x[0]) + str(x[-2])
    total = int(digit) + int(total)
print(total)
    