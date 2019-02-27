import random

def response(answer):
    if answer == "yes" or answer == "Yes" :
      rolldice()
    else:
      print("Maybe next time!")


def rolldice():
    randomnumb = random.randrange(1,7)
    print("You got number " + str(randomnumb) + "!")
    response(input("Would you like to roll the dice again? \n "))

response(input("Would you like to roll the dice? \n"))
