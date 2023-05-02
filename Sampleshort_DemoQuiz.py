# Project-On :Short Quiz Game
# Version : 1.0
# Purpose : Learning  if else condition
print("HELLO EVERYONE TO SHORT QUIZ !")
play = input("Do you want to play?(yes/no)\n")

if play.lower() != "yes":
    quit()

print("Let us begin!\n")
count = 0
ans = input("1] What does SSL stand for?\n")
if ans.lower() == "secure socket layer":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

ans = input("2] What does SSD stand for?\n")
if ans.lower() == "solis state drive":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

ans = input("3] What does HTTP stand for?\n")
if ans.lower() == "hyper text transfer protocol":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

ans = input("4] What does FTP stand for?\n")
if ans.lower() == "file transfer protocol":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

ans = input("5] What does TLS stand for?\n")
if ans.lower() == "transport layer security":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

    
print(f"Let's check how much you got is: {count}/5!\nYou got",count*25,"%")

#END
