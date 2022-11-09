from random import randint


def generate_cpf_body():
    body_digits = "".join([str(randint(0, 9)) for _ in range(9)])
    return body_digits
