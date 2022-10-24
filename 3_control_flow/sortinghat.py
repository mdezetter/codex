# Questions and input setup
q1 = int(input("Do you like Dawn or Dusk? \n1. Dawn \n2. Dusk\n"))
q2 = int(input("When I'm dead, I want people to remember me as: \n1. The Good \n2. The Great \n3. The Wise \n4. The Bold \n"))
q3 = int(input("Which kind of instrument most pleases your ear? \n1. The Violin \n2. The Trumpet \n3. The Piano \n4. The Drums \n"))

# Variables setup
gryffindor = 0
ravenclaw = 0
slytherin = 0
hufflepuff = 0

# Make it fancy intro
print("===============\n")
print("The Sorting Hat\n")
print("===============\n\n")

# Question 1 "Do you like dawn or dusk?"
if q1 == 1:
    gryffindor +=1
    ravenclaw +=1
elif q1 == 2:
    hufflepuff +=2
    slytherin +=2
else:
    print("Wrong input.\n")

# Question 2 "When I'm dead, I want people to remember me as:"
if q2 == 1:
    hufflepuff +=1
elif q2 == 2:
    slytherin +=1
elif q2 == 3:
    ravenclaw +=1
elif q2 == 4:
    gryffindor +=1
else:
    print("Wrong input\n")

# Question 3 "Which kind of instrument most pleases your ear?"
if q3 == 1:
    slytherin +=1
elif q3 == 2:
    hufflepuff +=1
elif q3 == 3:
    ravenclaw +=1
elif q3 == 4:
    gryffindor +=1
else:
    print("Wrong input\n")


# Ranking the houses
print("===============\n")
print("Congratulations you have been sorted into\n")
print("===============\n")
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("🦁 Gryffindor!\n")
elif ravenclaw >= slytherin and ravenclaw >= hufflepuff:
    print("🦅 Ravenclaw!\n")
elif hufflepuff >= slytherin:
    print("🦡 Hufflepuff!\n")
else:
    print("🐍 Slytherin!\n")

# Printing total scores for all houses
print("\nIf you're curious, here's how close you were to other houses!")
print(f"Gryffindor: {gryffindor}")
print(f"Slytherin: {slytherin}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Hufflepuff: {hufflepuff}\n")