# ROI Guessing Game
# Author: Stuart Hanson
# Date: 05/06/2020
# Contact: stuart_hanson@outlook.com


from datetime import datetime



# Show Time report was run
dateTime = datetime.now()
reportRun = dateTime.strftime("%d/%m/%Y")
print("###################################################" + "\n")
print("---------Report was run: " + reportRun + "----------" + "\n")



# Read the packs file into an array

f = open('confPack.txt', 'r+')
lines = [line for line in f.readlines()]
f.close()

# Initialise the File
fp = open('output.txt', 'w')
fp.writelines("")


# Looping the employees file and checking for which packs are needed

count = 0

with open("employees.txt") as fp: 
    for line in fp: 
        if 'Y,Y' in line:
            with open('output.txt', 'a') as fp:
                fp.writelines(line.rstrip() + ": " + lines[0].strip() + " + " + lines[1].strip() + "\n")
        elif 'Y' in line:
            with open('output.txt', 'a') as fp:
              fp.writelines(line.rstrip() + ": " + lines[0].strip() + "\n")
              
        if 'Y' not in line:
            with open('output.txt', 'a') as fp:
                fp.writelines(line.rstrip() + ": No Packs Required \n")



# Display the final results
with open("output.txt") as fp:
    for line in fp:
        count += 1
        print(line.rstrip())


