# Basic - Print all integers from 0 to 150.

for i in range(0, 151):
    print(i)
    
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

count = 5
while (count < 1001):
    if (count % 5 == 0):
        print(f"Multiple of 5 under 1001 is : {count}")
        count += 1
    else : count +=1
    
# Counting, the Dojo Way

for i in range(1, 101):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i % 5 ==0):
        print("Coding")
    else : print(i)

# Whoa. That Sucker's Huge

count = 0
sum = 0
while (count < 500001):
   sum += count
   count += 1

print(f"{sum}") 

# Countdown by Fours

for i in range(2018, -1, -4):
    print(i)
    
# Flexible Counter 

lowNum = input("Enter lowNum : \n")
HighNum = input("Enter HighNum : \n")
mul = input("Enter mul : \n")

for i in range (int(lowNum), int(HighNum)):
    if (i % int(mul) == 0):
        print(i)
