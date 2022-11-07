from ..src.validate_cpf import validate_cpf


def test_validate_cpf():
    cpf = "105.204.539-13"
    position = 0
    assert validate_cpf(cpf) == cpf[::-1][position]
