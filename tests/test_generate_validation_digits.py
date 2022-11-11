from ..src.validate_cpf import validate_cpf
from ..src.generate_cpf import generate_cpf


def test_generate_cpf():
    cpf = generate_cpf()
    assert cpf == validate_cpf(cpf).get("cpf")
    assert cpf[9:] == validate_cpf(cpf).get("cpf")[9:]  # validation digits
    assert len(cpf) == 11
