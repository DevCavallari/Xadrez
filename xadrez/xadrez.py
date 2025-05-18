

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

print("\nLista de peças registradas:")
for i, peca in enumerate(pecas, start=1):
    print(f"{i}. Nome: {peca['nome']} | Cor: {peca['cor']} | Posição: {peca['posição']}")
