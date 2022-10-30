import caca_palavras as cp

caminho_arquivo = 'codigo\cacapalavra.txt'
tamanho_matriz = 35


arquivo = open(caminho_arquivo, 'r')
caca_palavras = cp.montar_caca_palavras(arquivo, tamanho_matriz)
matriz_cp = caca_palavras[0]
palavras = caca_palavras[1]


cp.imprimir(matriz_cp)


for palavra in palavras:
    print(cp.localizar_palavra(matriz_cp, palavra))


