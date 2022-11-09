from ..src.validate_cpf import validate_cpf
from ..src.generate_validation_digits import generate_validation_digits
from ..src.generate_cpf_body import generate_cpf_body


def test_generate_cpf():
    cpf_body = generate_cpf_body()
    cpf = generate_validation_digits(cpf_body)

    assert cpf[:-2] == cpf_body
    assert cpf == validate_cpf(cpf)
    assert len(cpf_body) == 9
    assert len(cpf) == 11
