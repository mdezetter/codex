import random

question = input("Ask the magic 8 ball a question: ")
random = random.randint(1,9)

if random == 1:
    print("Yes - definitely.")
elif random == 2:
    print("It is decidedly so.")
elif random == 3:
    print("Without a doubt.")
elif random == 4:
    print("Reply hazy, try again.")
elif random == 5:
    print("Ask again later.")
elif random == 6:
    print("Better not tell you now.")
elif random == 7:
    print("My sources say no.")
elif random == 8:
    print("Outlook not so good.")
elif random == 9:
    print("Very doubtful.")
else:
    print("Error")