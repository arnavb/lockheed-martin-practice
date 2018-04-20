#Problem 5
with open("Prob05.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)

for i in content:
    print(i.split(","))
import math
