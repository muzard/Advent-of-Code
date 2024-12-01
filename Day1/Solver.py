f = open("d:\koulu\koodit\Advent of Code\Day1\input1.txt", "r")
rawData = f.read()
f.close()


leftSide = []
rightSide = []
lastAdded = "right"
lastCharWasSpace = False

numAdder = []
for char in rawData:
    if char == " " and not lastCharWasSpace or char == """\n""":
        num = int("".join(numAdder))
        if lastAdded == "right":
            leftSide.append(num)
            lastAdded = "left"
        else:
            rightSide.append(num)
            lastAdded = "right"
        numAdder = []
        lastCharWasSpace = True
    elif char == " ":
        pass
    else:
        numAdder.append(char)
        lastCharWasSpace = False

leftSide.sort()
rightSide.sort()

sum = 0

for i in range(len(leftSide)):
    sum += abs(leftSide[i] - rightSide[i])

print("total sum was:")
print(sum)