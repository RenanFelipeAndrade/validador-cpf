from calculate_digit import calculate_digit
from remove_mask import remove_mask
from split_cpf import split_cpf


def validate_cpf(cpf: str) -> dict[str, bool | str]:
    if type(cpf) != str:
        raise TypeError("Insira um cpf do tipo texto")

    clean_cpf = remove_mask(cpf)
    if (len(clean_cpf)) != 11:
        return {
            "is_valid": False,
            "cpf": cpf,
            "message": "O cpf deve conter 11 dígitos",
        }

    first_digit = calculate_digit(clean_cpf, position=0)
    second_digit = calculate_digit(clean_cpf, position=1)
    calculated_digits = first_digit + second_digit
    _, validation_digits = split_cpf(clean_cpf)

    if validation_digits != calculated_digits:
        return {
            "is_valid": False,
            "cpf": cpf,
            "message": "O cpf tem dígitos verificadores inválidos",
        }
    return {
        "is_valid": True,
        "cpf": cpf,
        "message": "O cpf é válido",
    }
