from .split_cpf import split_cpf


def validate_body(cpf: str):
    cpf_body, _ = split_cpf(cpf)
    for number in range(9):
        number_occurence = cpf_body.count(str(number))
        if number_occurence == 9:
            raise ValueError("O corpo do cpf não pode ser números repetidos")
    return cpf
