def prob(a,b):

    if a==1:
            proba = 0.2
            if b==1:
                 probb = 0.85
            elif b==2:
                 probb = 0.15

            else:
                print("Invalid Choice") 

            probab = proba * probb
            print("Probability of b given a:", probb)
            print("probability of both:", probb) 

    elif a==2:
            proba = 0.8
            if b==1:
                 probb = 0.02
            elif b==2:
                 probb = 0.98

            else:
                print("Invalid Choice") 

            probab = proba * probb
            print("Probability of b given a:", probb)
            print("probability of both:", probb) 
    else:
            print("Invalid Choice")

print("Person has strep throat?\n 1.Yes \n 2.No")
a = int(input("Enter your choice (1/2)"))

print("Person has tested positive ?\n 1.Yes \n 2.No")
b = int(input("Enter your choice (1/2)"))

print("Probabilities for a and b ")
prob(a,b)