import random

print("1) Easy : (1 to 100) - 10 Attempts")
print("2) Medium : (1 to 500) - 7 attempts")
print("3) Hard : (1 to 1000) - 5 attempts")
opt = int(input("Choose your difficulty : "))

if opt == 1:
    n = random.randint(1,100)
    attempts = 10

elif opt == 2:
    n = random.randint(1,500)
    attempts = 7

elif opt == 3:
    n = random.randint(1,1000)
    attempts = 5
else:
    print("Invalid Option !! Try Again.")
    exit()

guess = -1
guesses = 0
while(guess != n and attempts > guesses):
    guess = int(input("guess a number: ")) 
    guesses += 1

    if(guess > n):
        print("Lower Number Please")

    elif(guess < n):
        print("Higher Number Please")

if(guess == n):
    print(f"You Have guessed the number, {n} correctly in {guesses} attempt")
else:
    print(f"You Lost !! Correct Answer is : {n}")