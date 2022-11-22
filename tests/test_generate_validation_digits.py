from src.validate_cpf import validate_cpf
from src.generate_validation_digits import generate_validation_digits
from src.generate_cpf_body import generate_cpf_body
from src.calculate_digit import calculate_digit


def test_generate_validation_digits():
    cpf_body = generate_cpf_body()
    validation_digits = generate_validation_digits(cpf_body)
    first_digit = calculate_digit(cpf_body, position=0)
    second_digit = calculate_digit(cpf_body, position=1)
    cpf = cpf_body + validation_digits

    assert first_digit == validate_cpf(cpf).get("cpf")[9]
    assert second_digit == validate_cpf(cpf).get("cpf")[10]
    assert first_digit == cpf[9]
    assert second_digit == cpf[10]
    assert first_digit + second_digit == validation_digits
    assert cpf == validate_cpf(cpf).get("cpf")
    assert validate_cpf(cpf).get("is_valid")
    assert cpf[9:] == validate_cpf(cpf).get("cpf")[9:]  # validation digits
    assert len(cpf) == 11
    assert len(cpf[9:]) == len(validate_cpf(cpf).get("cpf")[9:])  # validation digits
