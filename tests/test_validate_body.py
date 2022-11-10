from ..src.validate_body import validate_body
from ..src.generate_cpf_body import generate_cpf_body
from ..src.split_cpf import split_cpf


def test_validate_body():
    cpf = generate_cpf_body()
    cpf_body, _ = split_cpf(cpf)
    basic_cpfs = [str(number) * 9 for number in range(9)]

    assert len(cpf_body) == 9
    assert validate_body(cpf_body).get("is_valid")
    assert validate_body(cpf_body).get("cpf") == cpf
    assert cpf_body not in basic_cpfs
