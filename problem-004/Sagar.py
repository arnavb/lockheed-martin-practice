def getFibNum(nThNum):
    nThNum = nThNum
    list = [0, 1]
    didNotReach = True
    while didNotReach:
        firstNum = list[len(list)-2:][0]
        secondNum = list[len(list)-2:][1]
        list.append(firstNum + secondNum)
        if(len(list) >= nThNum):
            didNotReach = False
    return list[len(list) - 1:][0]

with open("Prob04.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)

for hi in content:
    hiNum = int(hi)
    print(hi + " = " + str(getFibNum(hiNum)))    