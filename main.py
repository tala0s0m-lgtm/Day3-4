from sum import summation
from sub import subtraction
from average import average
from max import maximum

choice = int(input("Choose operation:\n1 - Add\n2 - Sub\n3 - max\n4 - Avg"))

match choice:
    case 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = summation(num1, num2)
        print(f"The sum is: {result}")

    case 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = subtraction(num1, num2)
        print(f"The difference is: {result}")

    case 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = maximum(num1, num2)
        print(f"The maximum is: {result}")

    case 4:
        list_of_numbers = input("Enter numbers separated by spaces: ")
        result = average(list_of_numbers)
        print(f"The average is: {result}")

    case _:
        print("Invalid choice.")