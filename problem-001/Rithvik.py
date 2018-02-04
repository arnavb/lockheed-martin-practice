with open("Prob01.Txt") as prob1:
    lines = prob1.readlines
lines = [x.strip() for x in lines]
number_of_lines = len(lines)
Number_of_times = lines[1]
extra = lines.pop(0)
for(x in extra):
    print()