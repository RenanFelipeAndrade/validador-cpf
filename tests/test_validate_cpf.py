from src.validate_cpf import validate_cpf
from src.remove_mask import remove_mask


def test_validate_cpf():
    cpf = "453.178.287-91"
    clean_cpf = remove_mask(cpf)
    assert validate_cpf(cpf).get("cpf")[-2:] == clean_cpf[-2:]
    assert validate_cpf(cpf).get("is_valid")
    assert remove_mask(validate_cpf(cpf).get("cpf")) == clean_cpf
    assert len(validate_cpf(cpf).get("cpf")) == len(cpf)
    assert len(validate_cpf(cpf).get("cpf")) == len(clean_cpf) + 3
