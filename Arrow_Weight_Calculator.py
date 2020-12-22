def start():
    print("What arrow are you shooting?\n")

    choice = input("> ")

    global user_arrow_name
    if choice == "Axis":
        user_arrow_name = choice
        axis_choice()

    elif choice == "FMJ":
        user_arrow_name = choice
        fmj_choice()

    else:
        try_again("You fucked up already? Holy fucking shit buddy...")
        start()

axis_400 = 9.0
axis_340 = 9.5
axis_300 = 10.7
axis_260 = 11.5

def axis_choice():
    print("What arrow spine will you be using?\n")

    choice = float(input("> "))

    if choice == 400 or choice == 340 or choice == 300 or choice == 260:
        global spine
        spine = (choice)
        def axis_weight():
            global arrow_weight
            if spine == 400:
                arrow_weight = axis_400
                arrow_measurement()
            elif spine == 340:
                arrow_weight = axis_340
                arrow_measurement()
            elif spine == 300:
                arrow_weight = axis_300
                arrow_measurement()
            elif spine == 260:
                arrow_weight = axis_260
                arrow_measurement()
        axis_weight()
    else:
        try_again("You're made out of spare parts aren't ya?")
        axis_choice()


fmj_400 = 10.2
fmj_340 = 11.3
fmj_300 = 12.0

def fmj_choice():
    print("What arrow spine will you be using?\n")

    choice = float(input("> "))
    if choice == 400 or choice == 340 or choice == 300:
        global spine
        spine = choice
        def fmj_weight():
            global arrow_weight
            if spine == 400:
                arrow_weight = fmj_400
                arrow_measurement()
            elif spine == 340:
                arrow_weight = fmj_340
                arrow_measurement()
            elif spine == 300:
                arrow_weight = fmj_300
                arrow_measurement()
        fmj_weight()
    else:
        try_again("That's not an available spine you idiot. My blind grandmother could have done this better.")
        fmj_choice()


def arrow_measurement():
    print("What is the length of your arrow?\n")

    choice = input("> ")

    x = choice.replace('.', '', 1).isdigit()
    global arrow_length
    if x == True:
        arrow_length = float(choice)
        tip_weight()
    else:
        try_again("You fucking dumbass.")
        arrow_measurement()


def tip_weight():
    print("What grain tips will you be using?\n")

    choice = input("> ")

    global tip_weight
    if choice.isdigit():
        tip_weight = float(choice)
        insert_choice()
    else:
        try_again("You can't measure grains in words.")
        tip_weight()


HIT_insert = 16
brass_insert_50 = 50
brass_insert_75 = 75

def insert_choice():
    print("Are you using an HIT or Brass insert?\n")

    choice = input("> ")

    global insert_weight
    if "HIT" in choice:
        insert_weight = HIT_insert
        arrow_wrap()
    elif choice == "Brass" or choice == "brass":
        print("Are you using 50 or 75 grains of brass?\n")

        choice = input("> ")

        if choice == "50":
            insert_weight = brass_insert_50
            arrow_wrap()
        elif choice == "75":
            insert_weight = brass_insert_75
            arrow_wrap()
        else:
            try_again("That's not an available option.")
    else:
        try_again("That's not an available option.")
        insert_choice()


# standard arrow wrap is typically 1gpi (4.5in here)
arrow_wrap = 4.5
def arrow_wrap():
    print("Are you using an arrow wrap?\n")
    choice = input("> ")

    global arrow_wrap_length
    if choice == "Yes" or choice == "yes":
        print("What is the length of your arrow wrap? Arrow wraps are typically 1 grain per inch.\n")

        choice = float(input("> "))

        arrow_wrap_length = choice
        vane_choice()

    elif choice == "No" or choice == "no":
        arrow_wrap_length = 0
        vane_choice()

    else:
        print("C'mon, it's a yes or no question. Don't make this harder than it needs to be.\n")
        arrow_wrap()


vane_list = ['Max Stealth', 'Max Hunter', 'Max 23', 'Pro Max', 'PM 2.0 Target']
max_stealth_vane = 9.2
max_hunter_vane = 7.5
max_23_vane = 5
max_pro_max_vane = 4.9
pm20_target_vane = 4.9

def vane_choice():
    print("What arrow vane will you be using? Your choices include:\n\nMax Stealth\nMax Hunter\nMax 23\nPro Max\nPM 2.0 Target\n")

    choice = input("> ")

    global vane_choice
    if choice in vane_list:
        vane_choice = choice
        if vane_choice == "Max Stealth":
            vane_choice = max_stealth_vane
        elif vane_choice == "Max Hunter":
            vane_choice = max_hunter_vane
        elif vane_choice == "Max 23":
            vane_choice = max_23_vane
        elif vane_choice == "Pro Max":
            vane_choice = max_pro_max_vane
        elif vane_choice == "PM 2.0 Target":
            vane_choice = pm20_target_vane

        print("How many vanes will be on you arrow?\n")

        choice = input("> ")

        global vane_number
        if choice.isdigit():
            vane_number = float(choice)
            nock_choice()

    else:
        try_again("Are you fucking kidding me?")
        vane_choice()


easton_x_nock_weight = 9
nockturnal_nock_weight = 25

def nock_choice():
    print("Are you using the standard X Nock or Nockturnals?\n")

    choice = input("> ")

    global nock_weight
    if "X Nock" in choice or "X nock" in choice or "x Nock" in choice or "x nock" in choice:
        nock_weight = easton_x_nock_weight
        finish()
    elif "Nockturnals" in choice or "nockturnals" in choice:
        nock_weight = nockturnal_nock_weight
        finish()
    else:
        try_again("That's not an available option.")

def try_again(why):
    print(why, "Please try again.\n")


def finish():
    total_arrow_weight = (arrow_weight * arrow_length) + tip_weight + insert_weight + arrow_wrap_length + (vane_number * vane_choice) + nock_weight
    print("\nAccording to all the information provided, you're total arrow weight is:", total_arrow_weight)


print("Hello there! Let's figure out how much your arrow weighs starting from front to back.\n")
start()
