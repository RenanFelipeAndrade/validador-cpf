from .generate_cpf_body import generate_cpf_body
from .generate_validation_digits import generate_validation_digits


def generate_cpf(amount=1) -> str:
    def generate_one_cpf():
        cpf_body = generate_cpf_body()
        digits = generate_validation_digits(cpf_body)
        cpf = cpf_body + digits
        return cpf

    if amount == 1:
        return generate_one_cpf()

    cpf_list = []
    for _ in range(amount):
        cpf_list.append(generate_one_cpf())
    return cpf_list
