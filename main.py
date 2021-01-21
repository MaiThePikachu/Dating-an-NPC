'''
-------------------------------------------------------------------------------
Name:		main.py
Purpose:	A dating simulator.

Author:	Soon Fah.M
Created:	date in 18/01/2021
------------------------------------------------------------------------------
'''

# Some variables for the game
boy = True
girl = True
char = 


# Welcome message
print("Welcome! This is a text based game in a sense. This isn't the type of dating sim with buttons. It's one where you have to type the answers. When the choices are printed they will have ' ' around them and then you'll be able to type one of the given answers. (Please don't type the ' '. Also check if you typed the answers correctly because I don't have anything that will prevent you from mispelling. If you spell wrong have fun getting thrown down a random story line. :3)")

# A lot of variable questions for making a partner
print()
mc = input("What is your name: ")
print()

char = input("Okay. Next up is who do you want to date? A 'boy' or a 'girl': ")

print()

print("Hmmmmm...Should I give you the power to name them? Would be easier so I don't need to make their name lol.")

print()

char_name = input("What do you want their name to be: ")

print()

# Pretty much the beginning of the story
print("Perfect! Now that we have that done you can start the story. This takes place in (I guess) your bedroom and you're playing a game on your computer. It was an oddly popular game because in a way it was ''magical''. Alas it was some first-person, futuristic yet medieval polygon game. It had a couple of bugs allowing you to clip through many of the games objects. Things like trees and entire buildings even. Your walking through the forest clipping though a couple trees out of boredom. All of a sudden some bushes start moving.")


# The boy route
if char == boy:
  print("A blur jumps out and lunges at your charater driving their sword into it's stomach. You roll your swivel chair (aka spinny chair) backwards from surprize wondering if this game really is buggy. You turn around the chair wondering if you saw what happened corretly when you hear a loud thump behind you.")

  print()

  option_1 = input("Do you 'turn_around' or do you 'stay': ")

  if option_1 == turn_around:
    print("???: Okay foolish human where did you send me.")
    print("*They hold a blade towards you*.")
    print("???: Who are you? Are you an apprentice to that wall phasing fool?")

    print("...")
    option_2 = input("")
  elif option_1 == stay:
    print("???: Hey you! Don't ignore me where am I?")

# The girl route
elif char == girl:
  print("A girl runs out of the bushes and collides with your character. You roll your swivel chair (aka spinny chair) backwards from surprize wondering if this game really is buggy. The girl tumbles out from the screen and drops to the ground.")
      
  print()

  print("???: Kyaaaa!")

  print()

  option_1 = input("'help_her' or ask  'who_are_you?': ")

  if option_1 == help_her:
    print()
