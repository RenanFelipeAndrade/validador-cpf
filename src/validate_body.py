from split_cpf import split_cpf


def validate_body(
    cpf: str,
) -> dict[str, bool | str]:
    cpf_body, _ = split_cpf(cpf)

    # has 9 repeated number
    for number in range(9):
        number_occurence = cpf_body.count(str(number))
        if number_occurence == 9:
            return {
                "is_valid": False,
                "cpf": cpf,
                "message": "O corpo do cpf não pode ser números repetidos",
            }

    return {
        "is_valid": True,
        "cpf": cpf,
        "message": "O corpo do cpf é válido",
    }
