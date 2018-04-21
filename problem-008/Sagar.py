with open("Prob08.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)

import datetime

for i in content:
    i = i.split(" ")
    dst = float(i[0]) * 1000000
    spd = float(i[1])
    secs = int(round((dst/spd) * 60 * 60, 0))
    lul = datetime.timedelta(seconds=secs)
    lul = str(lul).split(" ")
    lul.pop(1)
    lul.append("")
    lul.append("")
    lul[1], lul[2], lul[3] = lul[1].split(":")
    lul = list(map(int, lul))
    print("Time to Mars: " + str(lul[0]) + " days, " + str(lul[1]) + " hours, " + str(lul[2]) + " minutes, " + str(lul[3]) + " seconds")
