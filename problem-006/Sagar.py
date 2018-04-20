with open("Prob06.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)

dictionary = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel' ,'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}


for idx, i in enumerate(content):
    if i[0].isdigit() == False:
        chararr = list(i)
        limb = len(chararr)
        lastprint = ""
        for ind, cltr in enumerate(chararr):
            temp = cltr.upper()
            if temp != " ":
                print(dictionary[temp], end='')
                lastprint = dictionary[temp]
            else:
                print(" ", end='')
                lastprint = " "
            if lastprint != " " and ind < limb - 1:
                print("-", end='')
        print("")
