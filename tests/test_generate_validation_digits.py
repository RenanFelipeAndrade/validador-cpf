from ..src.generate_cpf_body import generate_cpf_body
from ..src.generate_validation_digits import generate_validation_digits


def test_generate_cpf():
    cpf_body = generate_cpf_body()
    cpf = generate_validation_digits(cpf_body)
