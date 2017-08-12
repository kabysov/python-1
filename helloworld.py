while True:
    age = int(input("Enter your name"))

    if (age >= 18) and (age <= 150):
        print("You are eligible to vote")
    else:
        print("Please come back in {} years".format(18 - age))
