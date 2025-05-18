pecas = []

while True:
    nome = input("Nome da peça (ex: Peão, Rainha): ")
    cor = input("Cor da peça (Branca ou Preta): ")
    posicao = input("Posição no tabuleiro (ataque ou defesa): ")

    peca = {
        "nome": nome,
        "cor": cor,
        "posição": posicao
    }

    pecas.append(peca)

    continuar = input("Deseja adicionar outra peça? (s/n): ").lower()
    if continuar != 's':
        break

print("\nPeças registradas:")
for i, peca in enumerate(pecas, start=1):
    print(f"{i}. Nome: {peca['nome']} | Cor: {peca['cor']} | Posição: {peca['posição']}")


excluir = input("\nDeseja excluir alguma peça? (s/n): ").lower()
if excluir == 's':
    num = int(input("Digite o número da peça que deseja excluir: "))
    if 1 <= num <= len(pecas):
        removida = pecas.pop(num - 1)
        print(f"Peça '{removida['nome']}' removida com sucesso!")
    

print("\nLista final de peças:")
for i, peca in enumerate(pecas, start=1):
    print(f"{i}. Nome: {peca['nome']} | Cor: {peca['cor']} | Posição: {peca['posição']}")
