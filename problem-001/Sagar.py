with open("Prob01.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

i = 0
timeLoop = 0
for line in content:
    if(i != 0):
        for i in range(0, 2):
            print(line)
    i = i + 1
print("pls kill me git")