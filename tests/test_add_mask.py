from ..src.add_mask import add_mask
from pytest import raises


def test_add_mask():
    cpf = "45317828791"
    # cpf =  "070.680.938-68"

    with raises(ValueError) as add_mask_error:
        add_mask(cpf[:4])

    assert add_mask(cpf) == "453.178.287-91"
    assert add_mask("453.178.287-91") == "453.178.287-91"
    assert add_mask("453178.287-91") == "453.178.287-91"
    assert add_mask("453178287-91") == "453.178.287-91"
    assert add_mask("45-3178-28791") == "453.178.287-91"
    assert len(add_mask(cpf)) == len(cpf) + 3
    assert add_mask_error.exconly() == "ValueError: O cpf precisa ter 11 dígitos"
