from .remove_mask import remove_mask


def split_cpf(cpf):
    cpf = remove_mask(cpf)
    body_digits, verification_digits = cpf[:9], cpf[9:-1]
    return body_digits, verification_digits
