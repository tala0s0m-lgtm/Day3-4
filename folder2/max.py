# max_function

def find_max(numbers):
    """
    Function to find the maximum number in a list
    """
    if not numbers:  
        return None
    
    max_value = numbers[0]  #  Assume the first element is the largest
    
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value


def find_max_of_two(a, b):
    """
    Function to find the maximum of two numbers
    """
    if a > b:
        return a
    else:
        return b


# Test 
if name == "main":
    # Test find_max function
    my_list = [10, 25, 3, 48, 19, 7]
    result = find_max(my_list)
    print(f"The maximum value in {my_list} is: {result}")
    
    # Test find_max_of_two function
    x, y = 15, 8
    result2 = find_max_of_two(x, y)
    print(f"The maximum value between {x} and {y} is: {result2}")