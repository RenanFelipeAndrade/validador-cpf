from ..src.generate_cpf import generate_cpf
from ..src.add_mask import add_mask
from ..src.validate_cpf import validate_cpf


def test_generate_cpf():
    cpf = generate_cpf()
    cpf2 = generate_cpf(with_mask=False)
    cpf_list = generate_cpf(amount=10, with_mask=False)

    assert len(cpf[:11]) == 11  # without validation digit
    assert len(cpf[12:]) == 2  # validation digit
    assert validate_cpf(cpf).get("is_valid")
    assert cpf == add_mask(validate_cpf(cpf).get("cpf"))
    assert len(cpf) == 14

    assert cpf2 != add_mask(cpf2)
    assert len(cpf2) + 3 == len(add_mask(cpf2))

    for cpf in cpf_list:
        assert len(cpf[:9]) == 9  # without validation digit
        assert len(cpf[9:]) == 2  # validation digit
        assert validate_cpf(cpf).get("is_valid")
        assert len(cpf) == 11
