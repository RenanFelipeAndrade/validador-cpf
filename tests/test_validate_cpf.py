from ..src.validate_cpf import validate_cpf
from ..src.remove_mask import remove_mask


def test_validate_cpf():
    cpf = "105.204.539-13"
    clean_cpf = remove_mask(cpf)
    assert validate_cpf(cpf)[-2:] == clean_cpf[-2:]
    assert validate_cpf(cpf) == clean_cpf
    assert len(validate_cpf(cpf)) == len(clean_cpf)
