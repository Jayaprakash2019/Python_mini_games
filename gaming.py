print("Welcome to the computer quiz")

asking = input("Do you want to play the game? ") #input function

if asking.lower() !="yes":
    quit()
print("Let's play")

score = 0

question1 = input("what does cpu stands for? ")

if question1.lower() == "central processing unit":
    print("correct")
    score = score+1
else:
    print("Incorrect")

question2 = input("what does ram stands for? ")

if question2.lower() == "random access memory":
    print("correct")
    score = score+1

else:
    print("Incorrect")

question3 = input("what does rom stands for? ")

if question3.lower() == "read only memory":
    print("correct")
    score = score+1

else:
    print("Incorrect")

question4 = input("what does ssd stands for? ")

if question4.lower() == "solid state drive":      #comparison operator
    print("correct")
    score = score+1

else:
    print("Incorrect")

print(f"Your score is {score}")                    #print function and f strings

print("Your percentage is " + str((score/4)*100) + "%")   #string concantenate