num1 = 42 # variable declaration , initialize integer
num2 = 2.3 # variable declaration, initialize float
boolean = True # variable declaration , initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary declaration
fruit = ('blueberry', 'strawberry', 'banana') # Tuple declaration
print(type(fruit)) # type check
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # add value
print(person['name']) # access value
person['name'] = 'George' # change value
person['eye_color'] = 'blue' # add value
print(fruit[2]) # log statement 

if num1 > 45: # if
    print("It's greater") # log statement
else: # else
    print("It's lower") # log statement

if len(string) < 5: #if 
    print("It's a short word!") # log statement
elif len(string) > 15: # elif
    print("It's a long word!") # log statement
else: # else
    print("Just right!") # log statement

for x in range(5): # for loop
    print(x) # log statement
for x in range(2,5): # for loop
    print(x) # log statement
for x in range(2,10,3): # for loop
    print(x)
x = 0 # while loop
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # delete the last element the list
pizza_toppings.pop(1) # delete the element with the index 1 in the list

print(person) # print the elements of the dictionary
person.pop('eye_color') # delete the element with the key 'eye_color'
print(person) # print the dictionary after modification

for topping in pizza_toppings: # looping the pizza_topping list and break in the last element in the list
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():# function declaration that prints 'hello' 10 times
    for num in range(10):
        print('Hello')

print_hello_ten_times()#invoke function print_hello_ten_times()

def print_hello_x_times(x):# function declaration that prints 'hello' x times
    for num in range(x):
        print('Hello')

print_hello_x_times(4)# invoke function print_hello_x_times() 4 times as the argument

print ( "spaaaace")

def print_hello_x_or_ten_times(x = 10):# function declaration that prints 'hello' in default 10 times if the user didn't specify the times argument
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()# invoke function with no times argument which means it will be executes 10 times by default
print_hello_x_or_ten_times(4)# invoke function with specified times (4)


# Bonus section

print(num3) # error cause num3 is not defined
num3 = 72 # num3 variable initialization
fruit[0] = 'cranberry'# error tuple object does not support item assignement
print(person['favorite_team']) # error 'favorite_team key is not defined in person dictionary
print(pizza_toppings[7]) # IndexError: list index out of range
print(boolean) # prints 'True' by default
fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
