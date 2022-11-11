from .generate_cpf_body import generate_cpf_body
from .generate_validation_digits import generate_validation_digits


def generate_cpf() -> str:
    cpf_body = generate_cpf_body()
    digits = generate_validation_digits(cpf_body)
    cpf = cpf_body + digits
    return cpf
