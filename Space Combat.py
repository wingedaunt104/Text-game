#This is going to be a text based game
print("This is a text based game based on outer space combat")
fullName = input("Press any key to proceed")
name_parts = fullName.split()
#These lines get the user's name
while True:
    fullName = input("Please enter your full name please: ")
    name_parts = fullName.split()
    if len(name_parts) >= 2:
        firstName = name_parts[0]
        print("OK " + firstName + ", now let's proceed.\n")
        break
    else:
        print("Invalid input. \n")
#this is an intro to the game
print("This is going to be a short text-based game\n")
print("You have ran out of fuel for your ship..you are also being boarded by an unknown species, your only option is an escape pod to get to the surface\n")
#while loop in order to get user input in the first question
while True:
    questionOne = input("You exit your room, which weapon will you acquire- the crowbar or sledgehammer: ")
    try:
        questionOne = str(questionOne)
        if questionOne == "crowbar":
            print("you've acquired the crowbar\n")
            break
        elif questionOne == "sledgehammer":
              print ("you've acquired the sledgehammer\n")
              break
        elif questionOne != "crowbar" or questionOne != "sledgehammer":
            print("please input either crowbar or sledgehammer\n")
#gives value error if answer is a number
    except ValueError:
        print("Invalid! Please enter a valid answer.\n")
print("You continue down a hallway filled with dim lights\n")
#while loop for question two of the game and contains all aspects from the first question
while True:
    questionTwo = input("There is a split into two different halls, do you choose to go- right or left: ")
    try:
        questionTwo = str(questionTwo)
        if questionTwo == "right":
            print("you've choosen to go right, but be weary " + firstName + " , gas levels here are high\n")
            break         #there will be break statements throughout my code which exits the loop after a question is chosen
        elif questionTwo == "left":
            print ("you've chosen to go left, carful " + firstName + " you might get into combat\n")
            break
        elif questionTwo != "right" or questionOne != "left":
            print("please input either right or left\n")
    except ValueError:
        print("Invalid! Please enter a valid answer.\n")
#I had two different question three's so I had to initialize both before creating the loops
questionThreeA = None
#while loop and prompt for questionThreeA if user answers right for question two
while questionTwo == "right" :
    questionThreeA = input("Since you chose to go right, gas levels are high, will you- challenge or falter?: ")
    try:
        questionThreeA = str(questionThreeA)
        
        if questionThreeA == "challenge":
            print(firstName + ", you've chosen to try and live through the gas, this was a rather better choice\n")
            break
        elif questionThreeA == "falter":
#player loses the game here 
            print(firstName + ", you've chosen to try and back away from the gas but you accidentally back into the creature and it tears your face off.....\n")
            break
        elif questionThreeA != "challenge" or questionThreeA != "falter":
#player prompted to choose one of the choices
            print("please enter either challenge or falter\n")
    except ValueError:
#player is prompted to choose a valid choice
        print("Invalid! Please enter a valid answer.\n")
#as said this is another initialization of the question before the prompt
questionThreeB = None
#while loop which occurs if the user answered left on question two
while questionTwo == "left":
    questionThreeB = input("Since you choose to go left, you hear growling and footsteps, will you- challenge or falter?: ")
    try:
        questionThreeB = str(questionThreeB)
        if questionThreeB == "challenge":
#player loses the game here 
            print("well " + firstName + ", you've gotten yourself into a real predicament, you're left with nowhere to run, the creatures surround you and eat you..\n")
            break
        elif questionThreeB == "falter":
            print("This was the smarter choice, now you're less likely to be caught by them\n")
            break
#player prompted to choose one of the choices
        elif questionThreeB != "challenge" or questionThreeB != "falter":
            print("please enter either challenge or falter\n")
    except ValueError:
#player is prompted to choose a valid choice
        print("Invalid! Please enter a valid answer.\n")
#initialization of question four A depending on if question three A was entered as 'challenge'
questionFourA = None
if questionThreeA == "challenge":
    while True:
        questionFourA = input("You go through the gas, but one of the creatures sees you after you exit the gas, and then runs towards you; will you use your - weapon or run: ")
        try:
            questionFourA = str(questionFourA)
#these are conditionals depending mostly on your choice in question one
            if questionFourA == "weapon" and questionOne == "crowbar":
                print("The creature is far too strong for a crowbar, and it snaps over its body; the creature then strangles you to death\n")
                break
            elif questionFourA == "weapon" and questionOne == "sledgehammer":
                print("The sledgehammer strikes the creature in the neck and crushes its windpipe; you are victorious for now..\n")
                break
            elif questionFourA == "run":
#player loses the game here
                print("You decide to run, but the creature chases you and jumps on your back; then it bites into your throat, killing you\n")
                break
            else:
#player is prompted to choose one of the choices(from here on out, every else block is structured like this)
                print("Please enter either 'run' or 'weapon'\n")
        except ValueError:
#player is prompted to choose a valid choice(frome here on out every except block is structured like this)
            print("Invalid! Please enter a valid answer.\n")
#initialization of question four b depending on if question three b was entered as falter
questionFourB = None
if questionThreeB == "falter":
    while True:
        questionFourB = input("You go back and find a vent, will you go into it or walk past it? please enter - vent or forward: ")
        try:
            questionFourB = str(questionFourB)
            if questionFourB == "vent":
                print("Good, this is the safest you'll be for now\n")
                break
            elif questionFourB == "forward":
#player loses game here
                print("You've gone forward and a creature comes and rips your head off..\n")
                break
            else:
                print("Please enter either 'vent' or 'forward'\n")
        except ValueError:
            print("Invalid! Please enter a valid answer.\n")
#question five a is initialized here and player is prompted depending on if question four A is entered as weapon and the first question was entered as sledgehammer
questionFiveA = None
if questionFourA == "weapon" and questionOne == "sledgehammer":
    while True:
        questionFiveA = input("You continue on and you see the escape pod but there are three creatures guarding it will you - fight or wait?: ")
        try:
            questionFiveA = str(questionFiveA)
            if questionFiveA == "wait":
                print("Smart choice two of the three creatures have moved off\n")
                break
            elif questionFiveA == "fight":
#player loses game here
                print("The monsters overwhelm you when you approach and rip you apart\n")
                break
            else:
                print("please enter either 'wait' or 'fight'")
        except ValueError:
            print("Invalid! Please enter a valid answer.\n")
#initialization and prompt of question five b depending on if question four b was entered as 'vent'
questionFiveB = None
if questionFourB == "vent":
    while True:
        questionFiveB = input("you go through the vent and have come an dead end will you try to open it or go up, please input either- 'up' or 'pry': ")
        try:
            questionFiveB = str(questionFiveB)

            if questionFiveB == "pry" and questionOne == "crowbar":
#first ending of the game is here
                print("You successfully pry open the vent and get to your pod and escape to the surface(part 2 coming soon)\n")
                break
            elif questionFiveB == "up":
                print("Good call you've escaped danger for now\n")
                break
#here is the only nested if statement to play out multiple scenarios
            elif questionFiveB == "pry" and questionOne == "sledgehammer":
                #initialization of question five b2 depending on if question five b was entered as pry and question one was entered as sledgehammer
                    questionFiveB2 = input("you hear the creatures coming are you going to keep prying or go up, please input either- 'pry' or 'up': ")
                    try:
                        questionFiveB2 = str(questionFiveB2)
                        if questionFiveB2 == "pry":
                            #player loses the game here
                            print("the sledgehammer couldn't open the vent from the angle you were in and the creature dragged you off\n")
                            break
                        elif questionFiveB2 == "up":
                            print("Good call the creatures are too big for the vent upwards, you're safe for now..\n")
                            break
                    except ValueError:
                          print("Invalid! Please enter a valid answer.\n") 
            else:
                print("please enter the choices in the quotes\n")
        except ValueError:
              print("Invalid! Please enter a valid answer.\n")
#initialization and the prompt of question six a depending on whether or not the player selects wait
questionSixA = None 
if questionFiveA == "wait":
    while true:
        questionSixA = input("There is only one creature left which is weaker and is examining your escape pod, would you like to wait for this one to leave like the rest or fight, enter either- 'wait' or 'fight'\n")
        try:
            questionSixA = str(questionSixA)
            if questionSixA == "wait":
                #player loses game
                print("Since you've waited too long more creatures sneak up on you and break your neck\n")
                break
            elif questionSixA == "fight":
                #second ending to the game
                print("You overpower this creature regardless of its weapon due to its weakest form, you then get into your pod and escape to the surface (part 2 coming soon)\n")
                break
            else:
                print("please enter either 'wait' or 'fight'\n")
        except ValueError:
                          print("Invalid! Please enter a valid answer.\n")
#initialization and the prompt of question six b depending on whether or not the player selects up it question fiv b or question five b2
questionSixB = None
if questionFiveB == "up" or questionFiveB2 == "up":
    while true:
        questionSixB = input("After going up through the vent you encounter a submachine gun and you see the monsters down below, will you take the gun or disregard it, please enter-'take' or 'leave'\n")
        try:
            questionSixB = str(questionSixB)
            if questionSixB == "leave":
                print("You take a few steps and the creatures hear you then leap up and kill you\n")
                break
            elif questionSixB == "take":
                print("The creatures see you take the gun, you then shoot all three of them and they collapse, you then run downstairs, get into your pod and then escape\n")
            else:
                print("please enter either 'take' or 'leave'\n")
        except ValueError:
                          print("Invalid! Please enter a valid answer.\n")
            
 
        

      
             
            
                
                
                                





        
        

            

        
    
          

            
        
