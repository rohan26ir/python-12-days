""" 
- Functions, 
- *args, 
- **kwargs, 
- Lambdas,
- Scope

"""

from typing import Callable

# Positional, Keyword, and Default Arguments

def calculate_total(
        price: float, 
        tax_rate: float, 
        discount: float
        ) -> float:
    """
    Calculate the total price after applying tax and discount.

    :param price: The original price of the item.
    :param tax_rate: The tax rate to be applied (default is 5%).
    :param discount: The discount to be applied (default is 0).
    :return: The total price after tax and discount.
    """
    total = price + (price * tax_rate) - discount
    return total

print(calculate_total(10, 0.5, 10))
# op: 5.0

# Variable Positional (*args) and Keyword (**kwargs) Arguments

def build_pipeline_step(
        step_name: str, 
        *args, 
        **kwargs) -> dict:
    
    """
    Consumes arbitrary positional flags and keyword configurations.
    """
    return {
        "step": step_name,
        "flags": args,
        "configuration": kwargs,
    }

step_meta = build_pipeline_step(
    "ingest", "verbose", "dry-run", timeout=30, retries=3
    )
print(f"Pipeline Config: {step_meta}")
# op: Pipeline Config: {'step': 'ingest', 'flags': ('verbose', 'dry-run'), 'configuration': {'timeout': 30, 'retries': 3}}


# First-Class Functions and Higher-Order Usage

def apply_transform(
        data: list[int], 
        operation: Callable[[int], int]
        ) -> list[int]:
    """
    Applies a transformation operation to each item in the data list.
    """
    return [operation(item) for item in data]

print(apply_transform([1, 2, 3, 4], lambda x: x * 2))  
# Op: [2, 4, 6, 8]


# Anonymous Functions (lambda)

raw_numbers = [1, 2, 3, 4, 5]
squared = apply_transform(raw_numbers, lambda x: x ** 2)
sorted_pairs = sorted(
    [
    (1, "z"), 
    (3, "a"), 
    (2, "m")
    ], 
    key=lambda item: item[1]
    )

print(f"Squared: {squared}")
print(f"Sorted by letter: {sorted_pairs}")
"""
op: 
Squared: [1, 4, 9, 16, 25]
Sorted by letter: [(3, 'a'), (2, 'm'), (1, 'z')]

"""