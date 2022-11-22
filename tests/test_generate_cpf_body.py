from src.generate_cpf_body import generate_cpf_body


def test_test_generate_cpf():
    cpf_body = generate_cpf_body()

    assert len(cpf_body) == 9
