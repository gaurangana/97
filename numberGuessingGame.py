import random
print("Number Guessing Game")
number= random.randint(1,9)
print(number)
chances= 0
print("guess a number between 1-9:- ")
while chances < 5:
    guess=int(input("enter your guess:- "))
    if(guess== number):
        print("Congratulations you won!")
        break
    elif(guess < number):
        print("ur guess is too low :( enter a higher number than",guess)

    else:
        print("you guess was too high... enter something less than ",guess)
    chances+=1
if(chances>= 5):
    print("you loose :( the number is ",number)

    