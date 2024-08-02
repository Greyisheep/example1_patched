def add(a, b):
    """Performs the addition operation on two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the input parameters a and b.
    """
    return a + b

def subtract(a, b):
    """Performs subtraction operation of two numbers.
    
    Args:
        a (int/float): The number from which another number will be subtracted.
        b (int/float): The number which will be subtracted from the first number.
    
    Returns:
        int/float: The result of the subtraction operation.
    """
    return a - b

def multiply(a, b):
    """Performs multiplication of two numbers.
    
    Args:
        a (int/float): The first number to multiply.
        b (int/float): The second number to multiply.
    
    Returns:
        int/float: The result of multiplication of a and b.
    """
    return a * b

def divide(a, b):
    """Divides the first parameter by the second parameter.
    
    Args:
        a (int or float): The dividend.
        b (int or float): The divisor. Must not be zero.
    
    Returns:
        float or str: The result of the division if successful, an error message if division by zero is attempted.
    """
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    """A simple calculator function.
    
    This function prints the menu of the calculator which includes Add, Subtract, Multiply and Divide operations.
    Then, asks the user to input the choice of operation, and two numbers to perform the selected operation.
    Finally, it prints the results of the operation.
    
    Args:
        None
    
    Returns:
        None: This function doesn't return anything, it just prints the result of the operation.
    """
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()