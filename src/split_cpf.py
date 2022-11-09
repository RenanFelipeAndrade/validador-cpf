from .remove_mask import remove_mask


def split_cpf(cpf: str):
    cpf = remove_mask(cpf)
    if len(cpf) < 9 or len(cpf) > 11:  # without validation digits
        raise ValueError("O cpf precisa ter 11 dígitos")
    # 9 + (len(cpf) % 9) --> validation digits after cpf body
    body_digits, verification_digits = cpf[:9], cpf[9 : 9 + (len(cpf) % 9)]
    return body_digits, verification_digits
