from random import randint

computer_number = randint(1, 100)

while True:
    player_input = input("Can you guess the number from 1 to 100:")
    if not player_input.isdigit():
        print("Please enter a number:")
        continue

    player_input_int = int(player_input)
    if player_input_int == computer_number:
        print("You win!")
        break
    elif player_input_int > computer_number:
        print("Too big.")
    elif player_input_int < computer_number:
        print("Too small.")
