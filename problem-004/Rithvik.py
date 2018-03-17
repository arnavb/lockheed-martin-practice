with open("Prob04.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)
for x in content:
    a = 1
    b = 1
    help_ = a
    if x == a:
        place = 0
    else:
        place = -2
        while(x != a):
            help_ = a
            a = a + b
            b = help_
            place = place + 1

    print(x + " = " + place)
        