from .remove_mask import remove_mask


def calculate_digit(cpf: str, position=0):
    cpf = remove_mask(cpf)
    body_digits, verification_digits = list(cpf[:9]), list(cpf[9:-1])
    print(body_digits, verification_digits)
    counter = 10 + position
    accumulator = 0
    if position > 0:
        body_digits.append(verification_digits[0])

    for digit in body_digits:
        accumulator += int(digit) * counter
        counter -= 1

    digit = str((accumulator * (10)) % (11))
    return digit
