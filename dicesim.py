from random import randrange
print("Welcome to Die Simulator")
choice = True
ch = True
while ch:
    no_die = int(input("Enter the number of die's: "))
    random_numbers = []

    for i in range(0, no_die):
        new_random_no = randrange(1, 7)
        random_numbers.append(new_random_no)


    for i in random_numbers:
        if i == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        if i == 2:
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        if i == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        if i == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        if i == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        if i == 6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
        print("\n")

    choice = input("Do you want to continue: (Y/N) ")
    if choice.upper() == "Y":
        ch = True
    else:
        ch = False
