# Cores utilizada no script
RED = "\033[1;31m"
GREEN = "\033[0;32m"
GREEN_T = "\033[92m"
RESET = "\033[0;0m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
GRAY = "\033[1;35m"

MENU = f"""{RED}
###############
[0] - DEPOSITAR
[1] - SACAR
[2] - EXTRATO
[3] - SAIR
###############{RESET}
"""
# limite 3 saques por dia
# limite de 500 reais por saque
# extrato


def main():

    SALDO = 0
    LIMITE = 500

    while True:

        print(MENU)
        opcao = int(input(f"{BLUE}Informe a opção desejada:{RESET} "))

        if opcao == 0:
            # depositar
            deposito = float(input(f"\n{YELLOW}Informe o valor a ser depositado:{RESET} "))
            i = 3
            while i <= 4:
                if deposito > 0:
                    print(f"{GREEN}Depósito realizado com sucesso!{RESET}")
                    SALDO += deposito
                else:
                    print("\n##Valor inválido.!##")
                    print("##Informe um valor maior que 0.##")
                    print(f"##Você tem mais {5 - i} tentativa(s).##")
                    deposito = float(input(f"\n{YELLOW}Informe o valor a ser depositado:{RESET} "))
                i += 1

        elif opcao == 1:
            # sacar
            s = 3
            while s <= 4:
                saque = float(input(f"\n{YELLOW}Informe o valor a ser sacado:{RESET} "))
                if saque <= SALDO and saque <= LIMITE:
                    print(f"{GREEN}Saque realizado com sucesso!{RESET}")
                    SALDO -= saque
                    s = 5
                elif saque > SALDO:
                    print(f"{RED}Saldo insuficiente.{RESET}")
                    print(f"Seu saldo atual é de {SALDO}")
                    s += 1
                elif saque > LIMITE:
                    print(f"\n{RED}Limite de saque excedido.{RESET}")
                    print(f"Seu limite de saque é de {LIMITE}")
                    s += 1
                else:
                    print(f"{RED}Valor inválido.{RESET}")
        elif opcao == 2:
            # extrato
            print("\n##############")
            print(f"{GREEN_T}Extrato:{RESET}")
            print(f"{YELLOW}Seu saldo é de {int(SALDO)}.{RESET}")
            print(f"{YELLOW}Seu limite de saque é de {LIMITE}.{RESET}")
            print("##############")
            pass
        elif opcao == 3:
            # sair
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
