from ..src.generate_cpf import generate_cpf
from ..src.validate_cpf import validate_cpf


def test_generate_cpf():
    cpf = generate_cpf()

    assert len(cpf[:-2]) == 9
    assert len(cpf[9:]) == 2
    assert cpf == validate_cpf(cpf)
    assert len(cpf) == 11
