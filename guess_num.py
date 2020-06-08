"""
Ask user for a number
1) check if num is secret num
2) if not say if their number is higher or lower
3) have an option to give up

"""
from random import randint

def main():
    name = ""
    num_list = ['1','2','3','4','5','6','7','8','9']
    count = 1

    while name == "":
        name = input("Hello.  Please Type in your Name: ")


    secret_num = randint(1,101)
    print("Hello {} Let's Play a Guessing Game.  I am thinking of a number from 1 to 100. Guess the number.".format(name))
    user_input = input("Type your Guess or type quit to quit the game: ")

    while True:
        if user_input.lower() == 'quit':
            print("The Secret Number was {}".format(secret_num))
            break
        elif user_input[0] in num_list and int(user_input) in range (1, 101):
            if int(user_input) == secret_num:
                print("Good Job {}! You have guessed the secret Number in {} guess(es)".format(name, count))
                break
            elif int(user_input) > secret_num:
                print("You have guessed {}.  It is higher then the secret number.".format(user_input))
                user_input = input("Type your Guess or type quit to quit the game: ")
                count += 1
            else:
                print("You have guessed {}.  It is lower then the secret number.".format(user_input))
                user_input = input("Type your Guess or type quit to quit the game: ")
                count += 1
        else:
            print("You have typed in an invalid response.")
            user_input = input("Type your Guess or type quit to quit the game: ")

    print("Thank you for playing the Number Guessing Game.")

if __name__ == "__main__" :
    main()