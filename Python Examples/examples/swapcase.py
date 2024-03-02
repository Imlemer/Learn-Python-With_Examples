
#                                                                            \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
#                                                                            \                                                   \
#                                                                            \  A       S  I  M  P  L  E      P  Y  T  H  O  N   \
#                                                                            \                                                   \
#                                                                            \                                                   \
#                                                                            \          S W A P C A S E    T U T O R I A L       \
#                                                                            \                                                   \
#                                                                            \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \



# Defining function

def swapcase():

    # Printing message

    print("Enter your sentence to swapcase!")

    # Saving user input as "x"

    x = input()
    if x is not None:
        capitalized = str(x).swapcase()
        print (f" Your swapcased sentence: {capitalized}")
        swapcase2 ()
    else:
        print("Please enter a sentence")
        swapcase2 ()



# This function gets called when the user got the swapcased sentence when he entered it. Infinite loop :0

def swapcase2():

    # Printing message

    print("Enter another sentence to swapcase")

    # Saving user input as "x"

    x = input()
    if x is not None:
        capitalized = str(x).swapcase()
        print (f" Your swapcased sentence: {capitalized}")
        swapcase2 ()
    else:
        print("Please enter a sentence")
        swapcase2 ()


# Activating the function. If you don't activate the function, it won't work and the command prompt will close

swapcase ()