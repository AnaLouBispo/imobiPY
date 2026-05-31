import csv

class Imovel:
    def calcular_aluguel(self):
        raise NotImplementedError(
            "Este método deve ser implementado pelas classes filhas."
        )


class Apartamento(Imovel):
    def __init__(self, quartos, garagem, possui_criancas):
        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):
        valor = 700

        if self.quartos == 2:
            valor += 200

        if self.garagem:
            valor += 300

        if not self.possui_criancas:
            valor *= 0.95

        return valor


class Casa(Imovel):
    def __init__(self, quartos, garagem):
        self.quartos = quartos
        self.garagem = garagem

    def calcular_aluguel(self):
        valor = 900

        if self.quartos == 2:
            valor += 250

        if self.garagem:
            valor += 300

        return valor


class Estudio(Imovel):
    def __init__(self, vagas):
        self.vagas = vagas

    def calcular_aluguel(self):
        valor = 1200

        if self.vagas >= 2:
            valor += 250

            if self.vagas > 2:
                valor += (self.vagas - 2) * 60

        return valor


def gerar_csv(valor_aluguel):
    with open("parcelas.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Parcela", "Valor"])

        for parcela in range(1, 13):
            escritor.writerow([parcela, f"R$ {valor_aluguel:.2f}"])

    print("\nArquivo parcelas.csv gerado com sucesso!")


def pedir_quartos():
    while True:
        try:
            quartos = int(input("Quantidade de quartos (1 ou 2): "))

            if quartos in [1, 2]:
                return quartos

            print("Digite apenas 1 ou 2.")

        except ValueError:
            print("Digite um número válido.")


def pedir_vagas():
    while True:
        try:
            vagas = int(input("Quantidade de vagas: "))

            if vagas >= 0:
                return vagas

            print("Digite um número maior ou igual a zero.")

        except ValueError:
            print("Digite um número válido.")


def pedir_parcelas():
    while True:
        try:
            parcelas = int(input("Parcelas do contrato (1 a 5): "))

            if 1 <= parcelas <= 5:
                return parcelas

            print("Digite um valor entre 1 e 5.")

        except ValueError:
            print("Digite um número válido.")


def main():
    CONTRATO = 2000

    print("======================================")
    print(" ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA ")
    print("======================================")

    nome = input("Nome do cliente: ")

    print("\nTipos de locação:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        quartos = pedir_quartos()
        garagem = input("Possui garagem? (s/n): ").lower() == "s"
        criancas = input("Possui crianças? (s/n): ").lower() == "s"

        imovel = Apartamento(quartos, garagem, criancas)

    elif opcao == "2":
        quartos = pedir_quartos()
        garagem = input("Possui garagem? (s/n): ").lower() == "s"

        imovel = Casa(quartos, garagem)

    elif opcao == "3":
        vagas = pedir_vagas()

        imovel = Estudio(vagas)

    else:
        print("Opção inválida.")
        return

    aluguel = imovel.calcular_aluguel()

    parcelas = pedir_parcelas()
    valor_parcela = CONTRATO / parcelas

    print("\n========== ORÇAMENTO ==========")
    print(f"Cliente: {nome}")
    print(f"Valor mensal do aluguel: R$ {aluguel:.2f}")
    print(f"Valor do contrato: R$ {CONTRATO:.2f}")
    print(f"Parcelamento: {parcelas}x de R$ {valor_parcela:.2f}")
    print("================================")

    gerar_csv(aluguel)


if __name__ == "__main__":
    main()


 