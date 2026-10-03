""" 
- Variables, 
- Data Types, 
- I/O 

"""

# Variables and Dynamic Typing

int_val: int = 42
float_val: float = 3.14159
string_val: str = "Modern Python"
bool_val: bool = True
none_val: None = None

print("int_val", int_val)
print("float_val", float_val)
print("string_val", string_val)
print("bool_val", bool_val)
print("none_val", none_val)

# Type Checking and Conversion
print("Type of int_val:", type(int_val))
print("Type of float_val:", type(float_val))
print("Type of string_val:", type(string_val))
print("Type of bool_val:", type(bool_val))
print("Type of none_val:", type(none_val))

# Arithmetic & Assignment Operations
a = 10
b =5
sum = a + b
print("Sum of a and b:", sum)
minus = a - b
print("Difference of a and b:", minus)
multiply = a * b
print("Product of a and b:", multiply)
divide = a / b
print("Division of a by b:", divide)
modulus = a % b
print("Modulus of a by b:", modulus)
power = a ** b
print("a raised to the power of b:", power)

# Standard Input / Output Handling

name = input("Enter your name: ")
print("I am", name)