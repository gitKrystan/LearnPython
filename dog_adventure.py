from sys import exit

#Initialize variables
def init():
    global bank, cart, store
    bank = 5
    cart = []
    store = {"dog bone": 4, "pickle": 3, "pizza": 1, "soda": 1}

#Stock text
wwdd = "Woof would you like to do?: "
invalid = "You didn't enter a valid choice."

#Define wait text
def wait():
    wait_text = raw_input("Press enter to continue.\n\n\n*****")

#Define do over text
def do_over(reason):
    print "*****\n\n\n%s Please start again." % reason
    wait()
    start()

#Define you win text
def win(reason):
    print ("*****\n\n\n%s Good dog! You get a pizza. "
        "Would you like to play again? (Y/N)\n\n\n*****") % reason

    again = raw_input(wwdd)

    while True:
        if again == "y" or again == "Y":
            start()
        elif again == "n" or again == "N":
            exit(0)
        else:
            print invalid
            again = raw_input(wwdd)

#Define game_over text
def game_over(reason):
    print ("*****\n\n\n%s Bad dog! Game over. "
        "Would you like to play again? (Y/N)\n\n\n*****") % reason
    again = raw_input(wwdd)

    while True:
        if again == "y" or again == "Y":
            start()
        elif again == "n" or again == "N":
            exit(0)
        else:
            print invalid
            again = raw_input(wwdd)

#Define the beginning of the game
def start():
    init()
    
    print ("\n\nYou are a small dog with above-average intelligence, "
        "speedy little legs, and a bank account containing $%d.") % bank
    print ("Your owner has opened the door to check the weather. You can: "
        "\n\t1: run outside"
        "\n\t2: stay indoors.")

    choice = raw_input(wwdd)

    if choice == "1":
        escape()
    elif choice == "2":
        win("Thanks for not running away.")
    else:
        do_over(invalid)

#Define escape
def escape():
    print ("\n\nOh, the great outdoors! So much to see, do, and smell. "
    "Would you like to: "
    "\n\t1: run across the street"
    "\n\t2: run down the sidewalk.")

    choice = raw_input(wwdd)

    if choice == "1":
        game_over("You get hit by a car.")
    elif choice == "2":
        sidewalk()
    else:
        print invalid
        escape()

#Define sidewalk story
def sidewalk():
    print ("\n\nYou are now running down the sidewalk. Feel the wind in your hair! "
        "Feel the pavement under those speedy little legs! "
        "Would you like to: "
        "\n\t1: run across the street"
        "\n\t2: run to the grocery store"
        "\n\t3: stop to sniff an area where another dog peed.")

    choice = raw_input(wwdd)

    if choice == "1":
        game_over("You get hit by a car.")
    elif choice == "2":
        grocery()
    elif choice == "3":
        game_over("Your owner catches you.")
    else:
        print invalid
        sidewalk()

#Define shopping experience
def shop():
    global bank

    while bank >= min(store.values()):
        print "\n\nThe following items are available for sale:"

        for item, price in store.iteritems():
            print "%s: $%d" % (item, price)

        choice = raw_input('What would you like to buy? (or choose "buy nothing"): ')

        if choice == "buy nothing":
            break
        elif choice in store and bank >= store[choice]:
            cart.append(choice)
            bank -= store[choice]
            del store[choice]
            print "\n\nYou now have $%d." % bank
        elif choice in store and bank < store[choice]:
            print "*****\n\nYou don't have enough money for that.\n\n*****"
            print "\n\nYou now have $%d." % bank
            wait()
        else:
            print invalid

    leave_grocery()

#Define grocery story
def grocery():
    global bank
    print ("\n\nYou've arrived at the grocery store. They don't allow dogs. "
        "Whom would you like to impersonate in order to get in?")

    costume = raw_input("Whoof would you like to be?: ")

    print ("\n\nDressed as %r, you enter the store. You have $%d to spend.") % (costume, bank)
    
    if bank >= max(store.values()):
        shop()
    else:
        print "Unfortunately, you don't have enough money to shop."
        leave_grocery()

#After grocery store
def leave_grocery():
    print "You are leaving the grocery with the following items: "
    print cart
    print ("\n\nWould you like to: "
        "\n\t1: run across the street"
        "\n\t2: return home.")

    choice = raw_input(wwdd)

    if choice == "1":
        game_over("You get hit by a car.")
    elif choice == "2":
        go_home()
    else:
        print invalid
        leave_grocery()

#Go home
def go_home():
    print ("You are such a tired dog. Time to go home. "
        "Your owner is so happy to see you, but he is hungry after searching for you for so long. "
        "Would you like to: "
        "\n\t1: give him your pizza"
        "\n\t2: run away again.")        

    choice = raw_input(wwdd)

    if choice == "1":
        pizza_test()
    elif choice == "2":
        escape()
    else:
        print invalid
        go_home()

def pizza_test():
    print "You are such a sweet doggy to give away your pizza."

    if "pizza" in cart:
        win("Thanks for the pizza.")
    else:
        game_over("You lied! You don't have any pizza!")

#Start the game
start()