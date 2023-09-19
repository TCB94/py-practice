#Tested on 3.10.6, it should work at least on Python 3+ or 3.10.
import time
print("Hi, everyone! It's DS here.")
loopresponse = True
shouldquit = False
#Experimenting loop responses until the user answers "yes" or "no" instead of quitting
while loopresponse == True and shouldquit != True:
    try:
        choice = input('''\nDo you want to hear my story of how Python is easy to understand in my opinion?
        (Answer "yes or "no".) ''')
##choicecon is used to convert the user's choice to lowercase.
        choicecon = choice.lower()
        if choicecon == "yes":
            loopresponse = False
            print("\nAlright, here goes!")
            time.sleep(2.5)
            print("\nScratch helped me to understand coding languages.")
            time.sleep(2.5)
            print("\nAt some point, in my life, I learned how to use HTML and Python.")
            time.sleep(3.5)
            print("\nHowever, Python seems very easy to me because of the variables, ifs,")
            print("and other coding values!")
            time.sleep(4.5)
            print("\nSo, I'm giving Scratch a pat on the head for helping me understand")
            print("program languages, even though I don't use it anymore.")
            time.sleep(4.5)
            print("\nAnd I learned how to program math, too! O.o")
            time.sleep(3.5)
            print("\nFor example, I can do 9 * 5!")
            print(9 * 5)
            print("And the answer is right there lol")
            time.sleep(3.5)
            print("\nAnd, by the way, I'm thinking to learn Django to complete Scrover 2.0! O.o")
            time.sleep(3.5)
            print("\nWelp, thanks for reading my code, have a good day!")
            time.sleep(3.5)
            shouldquit = True

        elif choicecon == "no":
            loopresponse = False
            print("\nAlright. When you're ready to hear my story, do let me know!")
            print("\nFor now, see you later!")
            time.sleep(3.5)
            shouldquit = True
    
    except:
        print('''\nI apologize, you typed in an invalid input.''')
        loopresponse = True
#just something to prevent question spam bugs, if it ever works
if shouldquit == True:
    exit()
