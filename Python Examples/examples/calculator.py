


#                                                                            \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
#                                                                            \                                                   \
#                                                                            \  A       S  I  M  P  L  E      P  Y  T  H  O  N   \
#                                                                            \                                                   \
#                                                                            \                                                   \
#                                                                            \      C A L C U L A T O R    T U T O R I A L       \
#                                                                            \                                                   \
#                                                                            \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \



# Defining our function:

def calculator():

    # Console message

    print("This is a calculator! Enter the first number!")

    # Asking the user to type in the first number and saving it as "x"

    x = input()

    # "Try" means that the code tries to execute the program, and if its not successfull then it prints out an error

    try:


        # Message appears in console

        print("Enter the method (+, -, * or /) !")

        # Asking the user to enter the method and saving it as "y"

        y = input()

        # Message appears in console

        print("Enter the second number!")

        # Asking the user to type in the first number and saving it as "x"

        z = input()

        # If the chosen method(y) was "+"

        if y == "+":

            # Perform addition, add z to x

            answer = float(x) + float(z)
            print(f"{answer}")

        # If the chosen method(y) was "-"

        elif y == "-":

            # Perform substraction, substract z from x

            answer = float(x) - float(z)
            print(f"{answer}")

        # If the chosen method(y) was "*"

        elif y == "*":

            # Perform multiplication, multiply x by z

            answer = float(x) * float(z)
            print(f"{answer}")

        # If the chosen method(y) was "/" or ":"

        elif y == "/" or y == ":":

            # Perform multiplication, divide x by z

            answer = float(x) / float(z)
            print(f"{answer}")


    # except ValueError means that if x or z aren't Integers Or Floats, or if the method is invalid(not +, -, *, / or :) it will print out an error.
    # Integer is a whole number, while Float isn't.
    # Ex: int(5), float(6.08). We will meet other types in later examples

    except ValueError:
        print("Numbers must be Integers, Method must be +, -, * or /")

# Activating the function. If you don't activate the function, it won't work and the command prompt will close

calculator ()
        