with open("Prob03.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)
for thing in content:
    thing = thing.split()
    print(str(int(thing[0]) + int(thing[1])) + ' ' + str(int(thing[0]) * int(thing[1])))