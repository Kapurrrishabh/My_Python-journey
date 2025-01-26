import random

lowest=1
highest=100
answer=random.randint(lowest,highest)
print("-----------Welcome to the Python number guessing game---------")
print(f"Guess the number between{lowest} and {highest}")
is_running=True
while is_running:
    guess=int(input("enter your guess"))
    if(guess<lowest or guess>highest):
        print("out of bound!")
    elif(guess>answer):
        print("Too hight! try something lower")
    elif(guess<answer):
        print("Too low guess something higher")
    elif(guess==answer):
        print("Congrats! thats the right answer")
        is_running=False
    

