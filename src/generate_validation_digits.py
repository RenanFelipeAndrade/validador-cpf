from .calculate_digit import calculate_digit


def generate_validation_digits(cpf_body: str):
    first_digit = calculate_digit(cpf_body, position=0)
    cpf = cpf_body + first_digit
    second_digit = calculate_digit(cpf, position=1)
    cpf += second_digit
    print(cpf, cpf_body, first_digit, second_digit)
    return cpf
