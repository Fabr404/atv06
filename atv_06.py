# Função para receber e exibir o nome completo
def nome_completo():
    primeiro_nome = input("Digite o primeiro nome: ")
    sobrenome = input("Digite o sobrenome: ")
    
    completo = primeiro_nome + " " + sobrenome
    print("Nome completo:", completo)

# Chama a função
nome_completo()
