import re
from typing import Callable

# генератор, який шукає числа у тексті
def generator_numbers(text: str):
    for numbers in re.findall(r"\s(\d+\.\d+|\d+)\s", text):
        yield float(numbers)

# обчислення загальної суми чисел у вхідному рядку 
def sum_profit(text: str, func: Callable):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
