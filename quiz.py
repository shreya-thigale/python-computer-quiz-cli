print("Welcome to my Computer Quiz!")
playing = input("Do you want to play my game? ")

if playing.lower() != "yes":
    quit()

print("Okay, Let's play 😁")
score = 0

answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print("CORRECT🎉🥳")
    score+=1
else:
    print("INCORRECT")

answer = input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("CORRECT🎉🥳")
    score+=1
else:
    print("INCORRECT")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("CORRECT🎉🥳")
    score+=1
else:
    print("INCORRECT")

answer = input("What does PSU stand for?")
if answer.lower() == "power supply unit":
    print("CORRECT🎉🥳")
    score+=1
else:
    print("INCORRECT")

answer = input("What does SSD stand for?")
if answer.lower() == "solid state drive":
    print("CORRECT🎉🥳")
    score+=1
else:
    print("INCORRECT")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 5) * 100)+ "%")