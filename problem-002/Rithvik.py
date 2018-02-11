with open("Prob02.in.txt") as f:
    content = f.readlines()
nola = content.pop(0)
content = [x.strip() for x in content]
for y , value in enumerate in content:
    x = y.split()
    content[y] = x
for x in range(0, int(nola)):
    print(content[x].pop(0))
