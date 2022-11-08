from .calculate_digit import calculate_digit
from .remove_mask import remove_mask
from .split_cpf import split_cpf


def validate_cpf(cpf: str):
    if type(cpf) != str:
        raise TypeError("Insira um cpf do tipo texto")

    clean_cpf = remove_mask(cpf)
    if (len(clean_cpf)) != 11:
        raise ValueError("Insira um cpf de tamanho válido")
    first_digit = calculate_digit(cpf, position=0)
    second_digit = calculate_digit(cpf, position=1)
    body_digits, _ = split_cpf(clean_cpf)
    return body_digits + first_digit + second_digit
