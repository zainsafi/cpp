# while loop with condition

secret_number = 5
guessed_number = 0
while guessed_number != secret_number:
    guessed_number = int(input("Guess a number betwee 1 to 6: "))
    if(guessed_number != secret_number):
        print("Wrong number.Try again...")

print("You have guessed the correct number.Congrats...")