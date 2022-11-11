from .remove_mask import remove_mask
from .split_cpf import split_cpf


def add_mask(cpf: str) -> str:
    cpf = remove_mask(cpf)
    if len(cpf) != 11:
        raise ValueError("O cpf precisa ter 11 dígitos")
    _, validation_digits = split_cpf(cpf)

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{validation_digits}"
