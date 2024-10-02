def add(a, b):  # Define function to perform addition
    answer = a + b  # Calculate the sum of a and b
    print(str(a) + " + " + str(b) + " = " + str(answer))  # Print the formatted result of addition

def sub(a, b):  # Define function to perform subtraction
    answer = a - b  # Calculate the difference of a and b
    print(str(a) + " - " + str(b) + " = " + str(answer))  # Print the formatted result of subtraction

def mul(a, b):  # Define function to perform multiplication
    answer = a * b  # Calculate the product of a and b
    print(str(a) + " * " + str(b) + " = " + str(answer))  # Print the formatted result of multiplication

def div(a, b):  # Define function to perform division
    answer = a / b  # Calculate the quotient of a and b
    print(str(a) + " / " + str(b) + " = " + str(answer))  # Print the formatted result of division


while True:  # Infinite loop to keep the program running until the user exits

    print("A.Addition")  # Display addition option to the user
    print("B.Subtraction")  # Display subtraction option to the user
    print("C.Multiplication")  # Display multiplication option to the user
    print("D.Division")  # Display division option to the user
    print("E.Exit")  # Display exit option to the user

    choice = input("Input your choice: ")  # Take the user's input for operation choice

    if choice == "a" or choice == "A":  # Check if the user chose addition
        print("Addition")  # Confirm addition operation
        a = int(input("input first number: "))  # Take the first number as input from the user
        b = int(input("input second number: "))  # Take the second number as input from the user
        add(a, b)  # Call the add function with the two inputs

    elif choice == "b" or choice == "B":  # Check if the user chose subtraction
        print("Subtraction")  # Confirm subtraction operation
        a = int(input("input first number: "))  # Take the first number as input from the user
        b = int(input("input second number: "))  # Take the second number as input from the user
        sub(a, b)  # Call the sub function with the two inputs

    elif choice == "c" or choice == "C":  # Check if the user chose multiplication
        print("Multiplication")  # Confirm multiplication operation
        a = int(input("input first number: "))  # Take the first number as input from the user
        b = int(input("input second number: "))  # Take the second number as input from the user
        mul(a, b)  # Call the mul function with the two inputs

    elif choice == "d" or choice == "D":  # Check if the user chose division
        print("Division")  # Confirm division operation
        a = int(input("input first number: "))  # Take the first number as input from the user
        b = int(input("input second number: "))  # Take the second number as input from the user

        if b == 0:  # Check if the second number is zero (to avoid division by zero)
            print("Error: Division by zero is not allowed.")  # Error message for division by zero
        else:
            div(a, b)  # Call the div function with the two inputs if no division by zero

    elif choice == "e" or choice == "E":  # Check if the user chose to exit the program
        print("Program ended")  # Confirm program termination
        quit()  # Exit the program
