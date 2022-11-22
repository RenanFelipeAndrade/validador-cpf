from validate_cpf import validate_cpf
from generate_cpf import generate_cpf


def main(choice: int) -> str:
    if choice == 1:
        cpf = input("Insira o cpf a ser validado (com ou sem máscara)\n> ")
        validated_cpf = validate_cpf(cpf)

        if validated_cpf.get("is_valid"):
            print("É valido")
        print(f'O cpf não é válido: {validated_cpf.get("message")}')
        return

    while True:
        amount = int(
            input("Insira a quantidade de cpfs a serem gerados (padrão: 1)\n> ")
        )
        with_mask = int(
            input(
                """Escolha com ou sem máscara (pontos e traço)
1- Com máscara
2- Sem máscara

> """
            )
        )
        if amount > 0 and (with_mask == 1 or with_mask == 2):
            break
        print("\n\nFaça escolhas válidas!\n\n")
    with_mask = True if with_mask == 1 else False

    cpf_list = generate_cpf(amount=amount, with_mask=with_mask)
    if len(cpf_list) == 1:
        return print(cpf_list[0])

    print("\n\nLista de cpfs gerados\n")
    for cpf in cpf_list:
        print(cpf)
    return


if __name__ == "__main__":
    while True:
        choice = int(
            input(
                """Escolha uma opção 
1- Validar cpf 
2- Gerar cpf válido

> """
            )
        )
        if not (type(choice) != int or choice < 1 or choice > 2):
            break

        print("\n\nEscolha uma opção válida!\n\n")

    main(choice)
