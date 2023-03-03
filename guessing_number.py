import random

top_of_range = input("Type a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("please enter the number greater than 0")
        quit()
else:
    print("Please enter the number")
    quit()

random_number = random.randint(0, top_of_range)
count = 0
while True:
    count +=1
    user_guess = input("Guess the number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter the number next time")
        continue
    
    if user_guess ==random_number:
        print("You got it!")
        break

    elif user_guess > random_number:
        print("You are above the number")
    
    else:
        print("You are below the number")

print("You have guessed the number in ", count, "count")
    

