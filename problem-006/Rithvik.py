from __future__ import print_function
Letters = {"A":"Alpha","N":"November","B":"Bravo","O":"Oscar","C":"Charlie" ,"P":"Papa","D":"Delta","Q":"Quebec","E":"Echo","R":"Romeo","F":"Foxtrot","S":"Sierra","G":"Golf","T":"Tango","H":"Hotel","U":"Uniform","I":"India","V":"Victor","J":"Juliet","W":"Whiskey","K":"Kilo","X":"Xray","L":"Lima","Y":"Yankee","M":"Mike","Z":"Zulu"}
with open("Prob06.in.txt") as file:
  lines = file.readlines()
output = ""
lines = [x.strip("\n") for x in lines]
testcases = int(lines.pop(0))
for val, x in enumerate(lines):
  output = ""
  if not(x.isdigit()):
        for z in x:
          if z == " ":
            output+= " "
          else:
            output += Letters[z.upper()]
            output += "-"
        output += " "
        output = list(output)
        for val, p in enumerate(output):
          if(p == " "):
            output.pop(val-1)
        output = "".join(output)
        print(output)
