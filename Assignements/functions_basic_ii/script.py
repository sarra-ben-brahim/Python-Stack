# Countdown function

def countdown(num):
    list_num = []
    for i in range(num, -1, -1):
        list_num.append(i)
    print(list_num)
        
countdown(10)

# Print and Return function

def print_and_return(list_input = []):
    print(list_input[0])
    return (list_input[1])

output = print_and_return([1,2])
print(output)

# First Plus Length function

def first_plus_lengh(list_input = []):
    length = len(list_input)
    sum = list_input[0] + length
    return sum

sum = first_plus_lengh([1,2,3,4,5])
print(sum)

# Values Greater than Second

from ast import Compare

def values_greater_than_second(list_input = []):
    if (len(list_input) < 2):
        return False
    list_output = []
    for i in range(0, len(list_input)):
        if (list_input[i]> list_input[1]):
             list_output.append(list_input[i])
    print(len(list_output))
    return list_output
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# Lengh and Value function

def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))