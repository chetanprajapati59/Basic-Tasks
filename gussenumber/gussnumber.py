import random
Computer_number = random.randrange(1,200)
userInput=(input("Enter your Name: "))
print("Hey, ", userInput," choose a number between 1 to 200 to guess the number.")
guess = 0
while guess != Computer_number:
    guess = int(input("Enter the number: "))
    if guess > Computer_number:
 
        print("Your guess number is too high")

    elif guess < Computer_number:
        print("Your guess number is too low")

    else:
        print("Congratulations, Your guess number is equal")