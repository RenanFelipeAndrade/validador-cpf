from ..src.split_cpf import split_cpf
from ..src.generate_cpf import generate_cpf
from pytest import raises


def test_split_cpf():
    cpf = generate_cpf(with_mask=False)
    cpf_body, validation_digits = split_cpf(cpf)

    with raises(ValueError) as split_cpf_error:
        split_cpf(cpf[:4])

    assert cpf_body == cpf[:9]
    assert validation_digits == cpf[9:]
    assert len(cpf_body) == len(cpf[:9])
    assert len(validation_digits) == len(cpf[9:])
    assert (
        split_cpf_error.exconly()  # exception as a str
        == "ValueError: O cpf precisa ter entre 9 a 11 dígitos"
    )
