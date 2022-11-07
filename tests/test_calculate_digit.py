from ..src.calculate_digit import calculate_digit


def test_calculate_digit():
    cpf = "105.204.539-13"
    assert calculate_digit(cpf) == cpf[-2]
    assert calculate_digit(cpf, position=1) == cpf[-1]
