from .calculate_digit import calculate_digit
from .remove_mask import remove_mask


def validate_cpf(cpf: str):
    if type(cpf) != str:
        raise TypeError("Insira um cpf do tipo texto")
    clean_cpf = remove_mask(cpf)
    first_digit = calculate_digit(cpf, position=0)
    second_digit = calculate_digit(cpf, position=1)
    return second_digit
