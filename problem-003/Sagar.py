with open("Prob03.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)
print(content)
