import re
from typing import Callable

def generator_numbers(text: str):
    """The generator func returns all float numbers found in the text."""
    for match in re.findall(r'\b\d+\.\d+\b', text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], None]) -> float:
    """Calculate the total sum of float numbers extracted
       from the text using the generator_numbers function."""
    return sum(func(text))

# "Example of usage"
# text = """Загальний дохід працівника складається з декількох частин: 1000.01 
#           як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")
