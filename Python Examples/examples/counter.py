


#                                                                            \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
#                                                                            \                                                   \
#                                                                            \  A       S  I  M  P  L  E      P  Y  T  H  O  N   \
#                                                                            \                                                   \
#                                                                            \                                                   \
#                                                                            \          C O U N T E R      T U T O R I A L       \
#                                                                            \                                                   \
#                                                                            \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \



# Defining function

def count_func():

    # Printing message

    print("Enter your sentence to count words!")

    # Saving user input as "sentence"

    sentence = input()

    # I didn't find a better way to do this, so I did it like that:

    # Here we count the spaces in "sentence"

    count = str(sentence).count(' ')

    # If the amount of spaces is greater than zero...

    if count != 0:

        # Add 1 to amount of spaces. If there is one space in the sentence "Hello world", then we just add 1 and get the word count

        counted = count + 1

        # Console message

        print (f" Words amount: {counted}")

        # Restart

        count_func2 ()
    else:

        # Console message

        print("Words amount: 1")

        # Restart

        count_func2 ()

# This function gets called when the user got the swapcased sentence when he entered it. Infinite loop :0

def count_func2():


    print("Enter your sentence to count words!")


    sentence = input()

    count = str(sentence).count(' ')


    if count != 0:

        counted = count + 1


        print (f" Words amount: {counted}")


        count_func2 ()
    else:


        print("Words amount: 1")


        count_func2 ()



# Activating the function. If you don't activate the function, it won't work and the command prompt will close

count_func ()