print("Welcome to JB Corp.")
print("Your mission is to find the breach.")

# Maze art
maze = """
         _________________________________________________________
        |                                                         |
        |   ___     ___     ___    |    ___    ___     ___    |   |
        |  |   |   |   |   |   |   |   |   |  |   |   |   |   |   |
        |  | S |---|   |---|   |---|---|   |--|   |---| E |   |   |
        |  |___|   |   |   |___|   |   |___|  |___|   |___|   |   |
        |                                                         |
        |    ___     ___     ___    |    ___    ___     ___    |   |
        |   |   |   |   |   |   |   |   |   |  |   |   |   |   |   |
        |---| E |---|   |---| S |---|---|   |--|   |---|   |---|   |
        |   |___|   |   |   |___|   |   |___|  |___|   |___|   |   |
        |                                                         |
        |    ___     ___     ___    |    ___    ___     ___    |   |
        |   |   |   |   |   |   |   |   |   |  |   |   |   |   |   |
        |---| S |---|   |---| E |---|---|   |--|   |---| S |---|   |
        |   |___|   |   |   |___|   |   |___|  |___|   |___|   |   |
        |                                                         |
        |_________________________________________________________|
"""

print(maze)

# Story and choices
choice1 = input('You\'re in the server room. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a server 404. There is a blinking light. Type "wait" to wait for it to turn green. Type "skip" to skip to next section. \n').lower()
  if choice2 == "wait":
    choice3 = input("You see three servers with blinking lights. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a server full of malware. Game Over.")
    elif choice3 == "yellow":
      print("You found the breached server! You Win!")
    elif choice3 == "blue":
      print("This server is heavily encrypted. Game Over.")
    else:
      print("You chose a server that doesn't exist. Game Over.")
  else:
    print("You get detected by the security system. Game Over.")
else:
  print("You fell into a trap. Game Over.")
