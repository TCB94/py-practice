#Tested on 3.10.6, it should work at least on Python 3+ or 3.10.
import time
print("Hi, everyone! It's DS here.")
choice = input('''Do you want to hear my story of how Python is easy to understand in my opinion?
(Answer "yes or "no".)''')
##choicecon is used to convert the user's choice to lowercase.
choicecon = choice.lower()
if choicecon == "yes":
    print("")
    print("Alright, here goes!")
    time.sleep(2.5)
    print("")
    print("Scratch helped me to understand coding languages.")
    time.sleep(2.5)
    print("")
    print("At some point, in my life, I learned how to use HTML and Python.")
    time.sleep(3.5)
    print("")
    print("However, Python seems very easy to me because of the variables, ifs,")
    print("and other coding values!")
    time.sleep(4.5)
    print("")
    print("So, I'm giving Scratch a pat on the head for helping me understand")
    print("program languages, even though I don't use it anymore.")
    time.sleep(4.5)
    print("")
    print("And I learned how to program math, too! O.o")
    time.sleep(3.5)
    print("For example, I can do 9 * 5!")
    print(9 * 5)
    print("And the answer is right there lol")
    time.sleep(3.5)
    print("")
    print("And, by the way, I'm thinking to learn Django to complete Scrover 2.0! O.o")
    time.sleep(3.5)
    print("")
    print("Welp, thanks for reading my code, have a good day!")
    time.sleep(3.5)
    exit()
    

elif choicecon == "no":
    print("")
    print("Alright. When you're ready to hear my story, do let me know!")
    print("")
    print("For now, see you later!")
    time.sleep(3.5)
    exit()
    
elif choicecon != "yes" or choicecon != "no":
    print('''Error: Please input "yes" or "no" next time.''')
    time.sleep(2.5)
    exit()