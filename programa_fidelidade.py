# Desenvolvido por Sérgio Henrique Reis Sá

from cliente import Cliente
from equipe import Equipe

# Função para adicionar clientes à equipe
def adicionar_clientes(equipe):
    clientes = [
        Cliente("João Silva", "joao@example.com"),
        Cliente("Maria Souza", "maria@example.com"),
        Cliente("Pedro Santos", "pedro@example.com"),
        Cliente("Sérgio", "sergio@example.com"),
        Cliente("Breno", "breno@example.com"),
    ]

    for cliente in clientes:
        equipe.adicionar_cliente(cliente)

# Função para simular compras dos clientes
def simular_compras(equipe):
    equipe.clientes[0].fazer_compra(50)
    equipe.clientes[1].fazer_compra(100)
    equipe.clientes[2].fazer_compra(75)
    equipe.clientes[3].fazer_compra(120)
    equipe.clientes[4].fazer_compra(90)

# Função para obter feedback dos clientes
def obter_feedback():
    feedback = input("Você gostaria de nos dar algum feedback? (S/N): ")
    if feedback.lower() == "s":
        comentario = input("Por favor, digite seu feedback: ")
        print("Obrigado pelo seu feedback! Valorizamos sua opinião.")
    else:
        print("Obrigado por usar nosso programa de fidelidade!")

# Função para listar todos os clientes
def listar_clientes(equipe):
    print("\nLista de Clientes:")
    for cliente in equipe.clientes:
        print(f"Nome: {cliente.nome}, E-mail: {cliente.email}, Pontos: {cliente.pontos}")

# Função para consultar pontos por e-mail
def consultar_pontos_por_email(equipe):
    email = input("Digite o e-mail do cliente: ")
    for cliente in equipe.clientes:
        if cliente.email == email:
            print(f"Pontos de {cliente.nome}: {cliente.pontos}")
            break
    else:
        print(f"Cliente com e-mail {email} não encontrado.")

# Função para exibir pontos totais
def exibir_pontos_totais(equipe):
    total_pontos = sum(cliente.pontos for cliente in equipe.clientes)
    print(f"Total de Pontos Acumulados por Todos os Clientes: {total_pontos}")

# Função principal do programa
def main():
    equipe = Equipe()
    adicionar_clientes(equipe)
    simular_compras(equipe)

    while True:
        print("\nOpções:")
        print("1 - Consultar pontos de um cliente por nome")
        print("2 - Consultar pontos de um cliente por e-mail")
        print("3 - Listar todos os clientes")
        print("4 - Exibir pontos totais acumulados")
        print("5 - Simular compra de um cliente")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_cliente = input("Digite o nome do cliente: ")
            for cliente in equipe.clientes:
                if cliente.nome == nome_cliente:
                    print(f"Pontos de {cliente.nome}: {cliente.pontos}")
                    obter_feedback()
                    break
            else:
                print(f"Cliente {nome_cliente} não encontrado.")
        elif opcao == "2":
            consultar_pontos_por_email(equipe)
            obter_feedback()
        elif opcao == "3":
            listar_clientes(equipe)
            obter_feedback()
        elif opcao == "4":
            exibir_pontos_totais(equipe)
            obter_feedback()
        elif opcao == "5":
            nome_cliente = input("Digite o nome do cliente: ")
            valor_compra = float(input("Digite o valor da compra: "))
            for cliente in equipe.clientes:
                if cliente.nome == nome_cliente:
                    cliente.fazer_compra(valor_compra)
                    print(f"Compra de {valor_compra} registrada para {cliente.nome}.")
                    print(f"Novos pontos de {cliente.nome}: {cliente.pontos}")
                    obter_feedback()
                    break
            else:
                print(f"Cliente {nome_cliente} não encontrado.")
        elif opcao == "6":
            print("Obrigado por usar nosso programa de fidelidade!")
            obter_feedback()
            print("Código criado por SERGIO HENRIQUE REIS SA")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
