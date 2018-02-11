with open("Prob03.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
nola = content.pop(0)
for x in content:
    x = x.strip(" ")
    x = x.split()
    add = int(x[0]) + int(x[1])
    multi = int(x[0]) * int(x[1])
    print( str(add) + " " + str(multi))
    