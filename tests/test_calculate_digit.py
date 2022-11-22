from src.calculate_digit import calculate_digit
from src.split_cpf import split_cpf
from src.generate_cpf import generate_cpf
from src.generate_cpf_body import generate_cpf_body
from src.generate_validation_digits import generate_validation_digits


def test_calculate_digit():
    cpf = generate_cpf()
    cpf_body, validation_digits = split_cpf(cpf)
    cpf_body2 = generate_cpf_body()
    validation_digits2 = generate_validation_digits(cpf_body2)

    assert calculate_digit(cpf_body, position=1) == validation_digits[1]
    assert calculate_digit(cpf_body, position=0) == validation_digits[0]
    assert calculate_digit(cpf_body2, position=1) == validation_digits2[1]
    assert calculate_digit(cpf_body2, position=0) == validation_digits2[0]
    assert calculate_digit(cpf) == cpf[-2]
    assert calculate_digit(cpf, position=1) == cpf[-1]
