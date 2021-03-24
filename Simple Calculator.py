def addition(x, y):
    return float(number1) + float(number2)

def subtract(x, y):
    return number1 - number2

def multiplication(x, y):
    return float(number1) * float(number2)

def division(x, y):
    return float(number1) / float(number2)

def squared(x):
    return float(number1) * float(number1)

def squareroot(x):
    return sqrt(float(number1))


print("Choose an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Squared")


user_choice = input("Select a number (1, 2, 3, 4 or 5):")

number1 = input("Choose your first number")
number2 = input("Choose your second number? Leave blank if using Square/Square root")



if user_choice == "1":
    print(float(number1), "added to", float(number2), "is", addition(number1, number2))
    
elif user_choice == "2":
    print(float(number1), "minus", float(number2), "is", subtract(number1, number2))
    
elif user_choice == "3":
    print(float(number1), "multiplied by", float(number2), "is", multiplication(number1, number2))
    
elif user_choice == "4":
    print(float(number1), "divided by", float(number2), "is", float(division(number1, number2)))
    
elif user_choice == "5":
    print(float(number1), "squared is", float(squared(number1)))

