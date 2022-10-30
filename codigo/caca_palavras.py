

def separar_palavra(string):
    lista = []
    lista.append('@')
    for i in range(len(string)):
        letra = string[i]
        if letra == '\n':
            continue
        lista.append(letra)
    lista.append('@')
    return lista



def imprimir(matriz):
    for lin in matriz:
        print(lin)



def adicionar_moldura(matriz, tamanho):
    matriz.append(['@'] * (tamanho + 2))
    return matriz 



def montar_caca_palavras(arquivo, tamanho):
    caca_palavras = []
    numeros = '1234567890'
    palavras = []
    linhas = arquivo.readlines()
    adicionar_moldura(caca_palavras, tamanho)
    for linha in linhas:
        if len(linha) == tamanho + 1:
            caca_palavras.append(separar_palavra(linha))
        verifica_linha = len(linha) < tamanho and linha[0] not in numeros
        if verifica_linha:
            linha = linha.replace('\n', '')
            palavras.append(linha)
    adicionar_moldura(caca_palavras, tamanho)
    return caca_palavras, palavras



def localizar_palavra(matriz, palavra):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == palavra[0]:
                achou = testar_sentidos(matriz, i, j, palavra)
                if achou:
                    return '------------------------'
            j += 1
        i += 1
    print(f'Palavra: {palavra}')
    return 'Palavra não encontrada\n'



def testar_sentidos(matriz, lin, col, palavra):
    norte = verifica_norte(matriz, lin, col, palavra)
    sul = verifica_sul(matriz, lin, col, palavra)
    leste = verifica_leste(matriz, lin, col, palavra)
    oeste = verifica_oeste(matriz, lin, col, palavra)
    nordeste = verifica_nordeste(matriz, lin, col, palavra)
    noroeste = verifica_noroeste(matriz, lin, col, palavra)
    sudeste = verifica_sudeste(matriz, lin, col, palavra)   
    sudoeste = verifica_sudoeste(matriz, lin, col, palavra)

    return norte or sul or leste or oeste or nordeste or noroeste or sudeste or sudoeste
    


def verifica_norte(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin - i][col] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Norte')
    return True



def verifica_sul(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin + i][col] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Sul')
    return True



def verifica_leste(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin][col + i] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Leste')
    return True



def verifica_oeste(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin][col - i] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Oeste')
    return True



def verifica_nordeste(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin - i][col + i] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Nordeste')
    return True



def verifica_noroeste(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin - i][col - i] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Noroeste')
    return True



def verifica_sudeste(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin + i][col + i] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Sudeste')
    return True



def verifica_sudoeste(matriz, lin, col, palavra):
    i = 1
    while i < len(palavra):
        letra = palavra[i]
        if matriz[lin + i][col - i] != letra:
            return False
        i += 1
    print(f'Palavra: {palavra}\nLinha: {lin}\nColuna: {col}\nDireção: Sudeste')
    return True


    