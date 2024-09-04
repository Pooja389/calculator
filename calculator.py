import os

# this function clears the screen
def clear_screen():
    os.system("cls")

print("welcome to the python calculator :")

number_1 = float(input("enter first number :"))
operation = input("enter one\n%\n/\n-\n+\n*\n")
number_2 = float(input("enter second number :"))

# function declaration
def calculator(n1,n2,symbol): # takes 3 parameter n1,n2,symbol
    if symbol == "%":
        result = n1 % n2
    elif symbol == "-":
        result = n1 - n2
    elif symbol == "+":
        result = n1 + n2
    elif symbol == "*":
        result = n1 * n2
    else:
        result = n1 / n2  
    # returns result 
    return(f"{result}")        

# calling the function with arguement
result = float(calculator(number_1,number_2,operation))

# printing out the result
print(f"{number_1} {operation} {number_2} = {result}")

end = False
while not end:
    ask = input((f"type 'y' to continue calculation with {result} and 'n' for new calculation 'e' for exit  : "))

    # continues the calculation with result
    if ask == "y":
        
        operation = input("enter one\n%\n/\n-\n+\n*\n")
        number_1 = result
        number_2 = float(input("enter second number :"))

        # calling out the function with arguement number1(result), number2,operation
        result = float(calculator(number_1,number_2,operation))
        print(f"{number_1} {operation} {number_2} = {result}")

    # generates a new calculation
    elif ask == "n":
       
       # clear out the screen
       clear_screen()
       print("welcome to the python calculator :")

       number_1 = float(input("enter first number :"))
       operation = input("enter one\n%\n/\n-\n+\n*\n")
       number_2 = float(input("enter second number :"))

       # calling the function with arguement
       result = float(calculator(number_1,number_2,operation))

       # printing out the result
       print(f"{number_1} {operation} {number_2} = {result}")
    else:
        print("bye bye")