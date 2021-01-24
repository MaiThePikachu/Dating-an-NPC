'''
-------------------------------------------------------------------------------
Name:		main.py
Purpose:	A dating simulator.

Author:	Soon Fah.M
Created:	date in 18/01/2021
------------------------------------------------------------------------------
'''

# Welcome message
print("~~~Date From Another World~~~")

print()

print("Welcome! This is a text based game in a sense. This isn't the type of dating sim with buttons. It's one where you have to type the answers. When the choices are printed they will have ' ' around them and then you'll be able to type one of the given answers. To make this easier I put all of them in lowercase. (Please don't type the ' '. Also check if you typed the answers correctly because I don't have anything that will prevent you from mispelling. If you spell wrong then you have to do it all over again. Don't forget punctuation...I've played through mulitple times to test lol.)")

# A lot of variable questions for making a partner.
print()
mc = input("What is your name: ")
print()

char = input("Okay. Next up is who do you want to date? A 'boy' or a 'girl': ")

print()

print("Hmmmmm...Should I give you the power to name them? Would be easier so I don't need to make their name lol.")

print()

char_name = input("What do you want their name to be: ")

print()

# Pretty much the beginning of the story.
print("Perfect! Now that we have that done you can start the story. (Please excuse how terrible my story telling is.) This takes place in (I guess) your bedroom and you're playing a game on your computer. It was an oddly popular game because in a way it was ''magical''. Alas it was some first-person, futuristic yet medieval polygon game. It had a couple of bugs allowing you to clip through many of the games objects. Things like trees and entire buildings even. Your walking through the forest clipping though a couple trees out of boredom. All of a sudden some bushes start moving.")

print()

# The boy route
if char == "boy":
  print("A blur jumps out and lunges at your charater driving their sword into it's stomach. You roll your swivel chair (aka spinny chair) backwards from surprize wondering if this game really is buggy. You turn around the chair wondering if you saw what happened corretly when you hear a loud thump behind you.")

  print()

  # The start of many options for the boy side of the story. (Don't mind the multiple print statements. It's confusing I know.)
  option_1 = input("Do you 'turn around' or do you 'stay': ")
  print()

  if option_1 == "turn around":
    print("???: Okay foolish human where did you send me.")
    print("*He holds a blade towards you*.")
    print("???: Who are you? Are you an apprentice to that wall phasing fool?")

    print()
    print("What do you want to say to him?")
    print("'who're you calling wall phasing fool!' ")
    option_2 = input("or 'what do you mean?': ")
    print()

    if option_2 == "who're you calling wall phasing fool!":
      print("???: You...You're the ghost who keeps scaring millions of people in my town that it's so unbearably quiet. It's practically a ghost town!")

      print()

      print("*There is a hissing and buzzing sound coming from your computer.*")

      print()

      print("???:What is that doing?")

      print()

      print("*He walks over cautiously and pokes the monitor with his blade You look concerned over to your amazing monitor you've played on for 5 years so far.*")

      print()

      print("???:What is this annoying sou-")

      print()

      print("*The monitor bursts into flames. You dread over the fact that the monitor was amazing an lasted for so long* (RIP monitor from the beginning of this game - now. Forgot I was here did you :3) *The boy panics and completely freezes the monitor and your tower.* (The pain continues.) *You sit and stare at the now ruined computer.*")

      print()

      print("???:Ah- Sorry I didn't mean to- Wait why am I apologizing to you! How did I get here!?")
      
      print()

      print("*The boy holds his blade toward you again.*")

      print()

      option_3 = input("'shrug' or 'ignore and continue to sulking': ")

      print()

      if option_3 == "shrug":
        print("???:*sigh*")
        
        print("*He sits down on the foor*")

        print("???:I give up...You're really are telling the truth and I have a sense for it. I guess I'm stuck here...My name is " + char_name + " what's yours...")

        print("*You tell him your name* (It's polite isn't it?)")

        print(char_name + ":Huh...Okay " + mc + " What are we going to do about that?")

        print("*Points his blade at the ruined computer set up.* (Aye time for quite a bit of information and a tiny minigame.) *You grab his blade and drop it to the ground. Then you drag him by the arm out of the house. You go to a nearby computer store.")

        print()

        print(char_name + ": Oi! Where are you dragging me- What are these things?")

        print()



  elif option_1 == "stay":
    print("???: Hey you! Don't ignore me where am I?")

    option_2 = input("What do you want to say to him? 'who and what are you?' or do you want to 'panic and throw a book at him'")






























# The girl route
elif char == "girl":
  print("A girl runs out of the bushes and collides with your character. You roll your swivel chair (aka spinny chair) backwards from surprize wondering if this game really is buggy. The girl tumbles out from the screen and drops to the ground.")
      
  print()

  print("???: Kyaaaa!")

  print()

  option_1 = input("'help her' or ask  'who are you?': ")

  if option_1 == "help her":
    print()
