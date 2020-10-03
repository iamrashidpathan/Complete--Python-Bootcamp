# Displaying Information


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


ex_row = [1, 2, 3]
display(ex_row, ex_row, ex_row)

# Accepting user input
result = int(input("Please enter a value: "))
print(result)
print(type(result))

# Validating user input


def user_choice():
    choice = 'WRONG'
    accept_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(accept_value)
    while (not choice.isdigit()) or (int(choice) not in accept_value):
        choice = input("Please enter a number between 0 and 10: ")
        # digit check
        if not choice.isdigit():
            print("Sorry, its not a digit")
        # range check
        elif int(choice) not in accept_value:
            print("value out of range")

    return int(choice)


print(user_choice())

# Simple user interaction


def display_game(game_l):
    print("Here is the current list: ")
    print(game_l)


def position_choice():
    choice = 'WRONG'
    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2)")
    if choice not in ['0', '1', '2']:
        print("Sorry, invalid choice")
    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list


def game_on_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N): ")

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand. please choose Y or N")

    if choice == 'Y':
        return True
    else:
        return False


game_on = True
game_list = [0, 1, 2]
while game_on:
    display_game(game_list)
    position = position_choice()
    replacement_choice(game_list, position)
    display_game(game_list)
    game_on = game_on_choice()

