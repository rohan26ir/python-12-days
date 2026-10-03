""" 
- Conditions, 
- loops, 
- Comprehensions, 

"""


# If-Elif-Else

x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# While Loop

counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1


# For Loop

for i in range(5):
    print("i:", i)  

# Comprehensions (List, Set, Dict)

  # List Comprehension

squared_numbers = [x**2 for x in range(10)]
print("Squared Numbers:", squared_numbers)

  # Set Comprehension

unique_numbers = {x for x in range(10) if x % 2 == 0}
print("Unique Even Numbers:", unique_numbers)

  # Dictionary Comprehension

squared_dict = {x: x**2 for x in range(5)}
print("Squared Dictionary:", squared_dict)