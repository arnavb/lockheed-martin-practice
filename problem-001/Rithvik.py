with open("Prob01.in.txt") as prob1:
    lines = prob1.readlines()

Not = lines[1:]
extra = lines.pop(0)

for x in range(0, int(extra)) :
    print(Not[x].replace("\n",""))
    print(Not[x].replace("\n",""))
