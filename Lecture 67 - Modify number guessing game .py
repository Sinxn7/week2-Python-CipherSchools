import random
winning_number=random.randint(1,100)
guess=1
game_over=False
while True:
    user_input=int(input("Enter a number between 1-100: "))
    if user_input == winning_number:
        print(f"YOU WIN!!, and you guessed this number in {guess} times")
        break
    else:
        if user_input<winning_number:
            print("too low")
        else:
            print('Too high')
        guess+=1
        continue
