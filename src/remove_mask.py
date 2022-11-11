def remove_mask(cpf: str) -> str:
    return "".join([digit for digit in cpf if digit.isnumeric()])
