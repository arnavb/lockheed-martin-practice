with open("Prob02.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)
for line in content:
    linearr = line.split()
    letter_to_pop = int(linearr[1])
    word = linearr[0]
    del linearr
    #pythons better
    word = word[:letter_to_pop] + word[letter_to_pop + 1:]
    print(word)