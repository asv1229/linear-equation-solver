sim = input("Is equation simeltaeneous? Enter 1 if yes, 0 if no ")
if sim == "1":
    simel = True
else:
    simel = False
if simel == False:
    print("solve for x in ax + b = c")
    a = float(input("What is a? "))
    b = float(input("What is b? "))
    c = float(input("What is c? "))

    if a == 0 and b == c:
        print("Cannot solve, infinite solutions")
    else:
        x = (c/a) - (b/a)
        print ("x is equal to ", x)
if simel == True:
    print("solve for x and y in ax + by = c and dx + ey = f")
    a = float(input("What is a? "))
    b = float(input("What is b? "))
    c = float(input("What is c? "))
    d = float(input("What is d? "))
    e = float(input("What is e? "))
    f = float(input("What is f? "))

    D = (a*e) - (d*b)

    if D != 0:
        x = ((c*e) - (f*b))/D
        y = ((a*f) - (d*c))/D
        print("X and y are, respectively,", x, "and", y)

    else:
        print("Unsolvable. When graphed, these lines are parallel, and therefore do not intersect.")