# comments in python in one line

"""
    multiple line comments
    line 1
    line 2

"""

# Primitive Data Types
number = 5
number_1 = 5.5

bool_1 = True
bool_2 = False

string = "This is a string."

# Composite Types
# Lists
list_1 = [1,2,3,4,True,False,"String",[1,2,3]]
list_1[7] = 123
list_1.append(True)
print(list_1)
print("Hello Everyone")

# Tuple
tuple_1 = (1,2,3,True,"Strings")
print(tuple_1)
list_2 = list(tuple_1)
print(list_2)
list_2.append(9001)
print(list_2)
tuple_1 = tuple(list_2)
print(tuple_1)

# Dictionary
dictionary_1 = {
    "name": "Bob",
    "age": 25,
    "is_married": False
}

dictionary_1["is_married"] = True
dictionary_1["last_name"] = "Jhons"

print(dictionary_1)


