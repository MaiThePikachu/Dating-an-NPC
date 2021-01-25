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

print("Welcome! This is a text based game in a sense. This isn't the type of dating sim with buttons. It's one where you have to type the answers. When the choices are printed they will have ' ' around them and then you'll be able to type one of the given answers. To make this easier I put all of them in lowercase. Please don't type the ' '. Also check if you typed the answers correctly because I don't have anything that will prevent you from mispelling. If you spell wrong then you have to do it all over again. Don't forget punctuation...I've played through mulitple times to test lol. (In a sense this is like the impossible quiz when you get things wrong.)")

print()

print("Just a warning: There is a cliff hanger after the quiz game because making an entire love story will take a long time and if I were to make it short and the character easily falls in love with you where's the fun in that?")

# A lot of variable questions for making a partner.
print()
mc = input("What is your name: ")
print()

char = input("Okay. Next up is who do you want to date? A 'boy' or a 'girl'(girl is currently unavailable so sorry you have to choose boy since it's the kinda finished part of the game): ")

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
    print("???: Okay foolish ghost where did you send me.")
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

     
      print("???:*sigh*")
        
      print("*He sits down on the foor*")

      print("???:I give up...You're really are telling the truth and I have a sense for it. I guess I'm stuck here...My name is " + char_name + " what's yours...")

      print("*You tell him your name* (It's polite isn't it?)")

      print(char_name + ":Huh...Okay " + mc + " What are we going to do about that?")

      print("*Points his blade at the ruined computer set up.* (Aye time a tiny minigame.) *You grab his blade and drop it to the ground. Then you drag him by the arm out of the house. You go to a nearby computer store.")

      print()

      print(char_name + ": Oi! Where are you dragging me- What are these things?")

      print()

      # Mini game 
      print("Okay so mini game time. Are you going to explain all things computers? No that would be too much so this is going to be a small multiple question quiz. Try your best to answer or you'll have to do the story all over again. All you need to do is...")

      print()

      print("TYPE THE LETTER <-Don't forget")

      print()

      print("How does a mouse convert distance for display?")
      print()
      print("A. DPI (dots per itch)")
      print("B. DPI (dots per inch)")
      print("C. DPS (diameter perimeter speed")
      print("D. PAD (perimeter area distance")

      question_1 = input("Which letter is correct: ")

      print()

      if question_1 == "B":
        print("Correct! On to the next question.")

        print()

        print("Question two. What is the smallest and fastest data storage on a computer?")
        print()

        print("A. Cashe")
        print("B. Ram")
        print("C. Hard Drive")

        question_2 = input("Which letter is correct: ")
          
        print()

        if question_2 == "A":
          print("Correct! On to the last question.")

          print()

          print("Last and final question.")
          print("What is the refresh on a computer monitor measured in?")

          print()

          print("A. Hurtz")
          print("B. Fartz")
          print("C. Hearts")
          print("D. Hertz")

          question_3 = input("Which letter is correct: ")

          print()

          if question_3 == "D":
            print("Congratulations! You've completed the game!")
            print("...")
            print("For now...")
            
          elif question_3 == "C":
            print("You were really that desperate? (Sorry for the insensitive joke.)")

          else:
            print("You were so close. Sorry to say this but you lost. Try a different answer next time!")




    else:
      print("???: In my home town there is some ghost going around and haunting all the people in my town. At the same time I managed to kill the ghost...")

      print()

      print("*He turned around to face the computer and it was buzzing and making weird sounds. He turns to face you*")

      print("???: What's that thing doing its so noisy.")

      print()

      print("*The monitor bursts into flames. You dread over the fact that the monitor was amazing an lasted for so long* (RIP monitor from the beginning of this game - now. Forgot I was here did you :3) *The boy panics and completely freezes the monitor and your tower.* (The pain continues.) *You sit and stare at the now ruined computer.*")

      print()

      print("???: Ah- Was that natural? I'm sorry.")

      print()

      print("*You shake your head. The boy infront of you panics over what to do.*")

      print()

      print("???: Oh! Ummmm...My name is " + char_name + ". We haven't introduced ourselves.")

      print()

      print("*You reluctantly give him an answer.*")

      print(char_name + ": " + mc + " is a nice name. So what do you want to do about that thing?")

      print()

      print("*You take his blade and place it on a table then drag him to a computer store nearby.*")

      # Mini game 
      print("Okay so mini game time. Are you going to explain all things computers? No that would be too much so this is going to be a small multiple question quiz. Try your best to answer or you'll have to do the story all over again. All you need to do is...")

      print()

      print("TYPE THE LETTER <-Don't forget")

      print()

      print("How does a mouse convert distance for display?")
      print()
      print("A. DPI (dots per itch)")
      print("B. DPI (dots per inch)")
      print("C. DPS (diameter perimeter speed")
      print("D. PAD (perimeter area distance")

      question_1 = input("Which letter is correct: ")

      print()

      if question_1 == "B":
        print("Correct! On to the next question.")

        print()

        print("Question two. What is the smallest and fastest data storage on a computer?")
        print()

        print("A. Cashe")
        print("B. Ram")
        print("C. Hard Drive")

        question_2 = input("Which letter is correct: ")
          
        print()

        if question_2 == "A":
          print("Correct! On to the last question.")

          print()

          print("Last and final question.")
          print("What is the refresh on a computer monitor measured in?")

          print()

          print("A. Hurtz")
          print("B. Fartz")
          print("C. Hearts")
          print("D. Hertz")

          question_3 = input("Which letter is correct: ")

          print()

          if question_3 == "D":
            print("Congratulations! You've completed the game!")
            print("...")
            print("For now...")
            
          elif question_3 == "C":
            print("You were really that desperate? (Sorry for the insensitive joke.)")

          else:
            print("You were so close. Sorry to say this but you lost. Try a different answer next time!")









  # The stay option for the boy.
  elif option_1 == "stay":
    print("???: Hey you! Don't ignore me where am I?")

    print()

    option_2 = input("What do you want to say to him? 'who and what are you?' or do you want to 'panic and throw a book at him': ")

    print()

    if option_2 == "who and what are you":
      print("???: What do you mean who and what are you? My name is " + char_name + " and I'm a human. Now I ask. Who and what are you?")

      print()

      print("*You introduce yourself and say that your human too*")

      print()

      print(char_name + ":" + mc + "...That's nice. So what am I doing here?")

      print()

      print("*You shrug*")

      print()

      print(char_name + ": Huh...I guess I'm stu-")

      print()

      print("*There is a hissing and buzzing sound coming from your computer.*")

      print(char_name + ": What is that sound?")

      print()

      print("*The monitor bursts into flames. You dread over the fact that the monitor was amazing an lasted for so long* (RIP monitor from the beginning of this game - now. Forgot I was here did you :3) *" + char_name + " panics and completely freezes the monitor and your tower.* (The pain continues.) *You sit and stare at the now ruined computer.*")

      print()

      print(char_name + ": Well the fire is out...Why are you sulking like that? Was the contraption really that important?")

      print()

      print("*You sigh and drop his blade to the ground and drag " + char_name + " by the arm to a nearby computer store.* (Multiple choice quiz time.)")

      print()

      # Multiple choice quiz
      print(char_name + ": Oi! Where are you dragging me- What are these things?")

      print()

      # Mini game 
      print("Okay so mini game time. Are you going to explain all things computers? No that would be too much so this is going to be a small multiple question quiz. Try your best to answer or you'll have to do the story all over again. All you need to do is...")

      print()

      print("TYPE THE LETTER <-Don't forget")

      print()

      print("How does a mouse convert distance for display?")
      
      print()
        
      print("A. DPI (dots per itch)")
      print("B. DPI (dots per inch)")
      print("C. DPS (diameter perimeter speed")
      print("D. PAD (perimeter area distance")

      question_1 = input("Which letter is correct: ")

      print()

      if question_1 == "B":
        print("Correct! On to the next question.")
      else:
        print("Oof! You have been dead ended due to incorrect answer.")

        print()

        print("Question two. What is the smallest and fastest data storage on a computer?")
        print()

        print("A. Cashe")
        print("B. Ram")
        print("C. Hard Drive")

        question_2 = input("Which letter is correct: ")
          
        print()

        if question_2 == "A":
          print("Correct! On to the last question.")
        else:
          print("Oof! You have been dead ended due to incorrect answer.")

          print()

          print("Last and final question.")
          print("What is the refresh on a computer monitor measured in?")

          print()

          print("A. Hurtz")
          print("B. Fartz")
          print("C. Hearts")
          print("D. Hertz")

          question_3 = input("Which letter is correct?")

          print()

          if question_3 == "D":
            print("Congratulations! You've completed the game!")
            print("...")
            print("For now...")
            
          elif question_3 == "C":
            print("You were really that desperate? (Sorry for the insensitive joke.)")

          else:
            print("You were so close. Sorry to say this but you lost. Try a different answer next time!")




    elif option_2 == "panic and throw a book at him":
      print("*The boy slashes the book into a million fluttering shards. After a moment of silence he starts laughing.*")

      print("???: Hahaha! That was so pathetic. I guess you aren't the ghost from my home town then. They are so weird because they just walk through anything and everything.")

      print()

      print("???: ...")

      print()

      print("???: Soooooo...What's your name? Mine is " + char_name + ".")

      print()

      print("*You reluctantly tell them your name. (It's only polite.)")

      print(char_name + ": " + mc + " is a really nice name. It was nice to meet you but I should get going back- Oh yeah! How did I get here?")

      print()

      print("*He frantically looks around your room for a portal that isn't there. After a couple seconds of his searching your computer goes off and starts to spark and burn. " + char_name + " put out the flames with what seemed like ice magic on reflex. Sadly accidentally freezing your shiny RGB tower. (RIP that. OH! Ummmm...HI! You forgot I was narrator. :3) You start to sulk a little over your now ruined computer. Thankfuly you saved up a lot of money since you were planning to by some upgrades for you computer.*")

      print(char_name + ": Ah- Was that normal for whatever that was.")

      print("*You shake your head and grab his arm. He starts to flush a bright pink.*")

      print(char_name + ": U-ummmmmm..." + mc + "... What are you doing?")

      print()

      print("*You grab his blade and place it on a table. Then you drag " + char_name + " to a nearby computer store since you just couldn't leave him at home. (To possibly break more things. Also hey quiz time!)")

      # Mini game 
      print("Okay so mini game time. Are you going to explain all things computers? No that would be too much so this is going to be a small multiple question quiz. Try your best to answer or you'll have to do the story all over again. All you need to do is...")

      print()

      print("TYPE THE LETTER <-Don't forget")

      print()

      print("How does a mouse convert distance for display?")
      print()
      print("A. DPI (dots per itch)")
      print("B. DPI (dots per inch)")
      print("C. DPS (diameter perimeter speed")
      print("D. PAD (perimeter area distance")

      question_1 = input("Which letter is correct: ")

      print()

      if question_1 == "B":
        print("Correct! On to the next question.")

        print()

        print("Question two. What is the smallest and fastest data storage on a computer?")
        print()

        print("A. Cashe")
        print("B. Ram")
        print("C. Hard Drive")

        question_2 = input("Which letter is correct: ")
          
        print()

        if question_2 == "A":
          print("Correct! On to the last question.")

          print()

          print("Last and final question.")
          print("What is the refresh on a computer monitor measured in?")

          print()

          print("A. Hurtz")
          print("B. Fartz")
          print("C. Hearts")
          print("D. Hertz")

          question_3 = input("Which letter is correct: ")

          print()

          if question_3 == "D":
            print("Congratulations! You've completed the game!")
            print("...")
            print("For now...")
            
          elif question_3 == "C":
            print("You were really that desperate? (Sorry for the insensitive joke.)")

          else:
            print("You were so close. Sorry to say this but you lost. Try a different answer next time!")



# The girl route
elif char == "girl":
  print("A girl runs out of the bushes and collides with your character. You roll your swivel chair (aka spinny chair) backwards from surprize wondering if this game really is buggy. The girl tumbles out from the screen and drops to the ground.")
      
  print()

  print("???: Kyaaaa!")

  print()

  option_1 = input("'help her' or ask  'who are you?': ")

  if option_1 == "help her":
    print()
