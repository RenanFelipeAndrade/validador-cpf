from .remove_mask import remove_mask
from ..src.split_cpf import split_cpf


def calculate_digit(cpf: str, position=0):
    body_digits, verification_digits = split_cpf(cpf)
    counter = 10 + position
    accumulator = 0
    if position > 0:
        body_digits += verification_digits[0]

    for digit in body_digits:
        accumulator += int(digit) * counter
        counter -= 1

    digit = str((accumulator * (10)) % (11))
    return digit
