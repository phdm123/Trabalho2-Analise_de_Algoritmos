def Guloso1():
    itens = []
    capacidade_atual = 0
    menor_peso = 10e16
    valor = 0
    valor_total = 0
    index = 0
    with open("large_scale/knapPI_1_100_1000_1") as arq: #Arquivo que será lido pelo algoritmo, caso queira ler outro, altere o nome do mesmo
        for linha in arq.readlines():
            peso = linha.strip().split(' ')[0]
            valor = linha.strip().split(' ')[1]
            if(int(peso) <= 0):
                continue
            itens.append([int(peso), int(valor), 0])
    arq.close()
    capacidade_max = itens.pop(0)[1]
    while True:
        for i in range(len(itens)):
            if(itens[i][1] < menor_peso and itens[i][2] == 0):
                menor_peso = itens[i][1]
                valor = itens[i][0]
                index = i
        if(capacidade_max > capacidade_atual + menor_peso):
            itens[index][2] = 1
            capacidade_atual += menor_peso
            valor_total += valor
        else:
            return [capacidade_max, capacidade_atual, valor_total, itens]
        menor_peso = 10e16

def Guloso2():
    itens = []
    capacidade_atual = 0
    peso = 0
    valor = 0
    valor_total = 0
    index = 0
    with open("large_scale/knapPI_1_100_1000_1") as arq: #Arquivo que será lido pelo algoritmo, caso queira ler outro, altere o nome do mesmo
        for linha in arq.readlines():
            peso = linha.strip().split(' ')[0]
            valor = linha.strip().split(' ')[1]
            if(int(peso) <= 0):
                continue
            relacao = int(valor)/int(peso)
            itens.append([int(peso), int(valor), 0, round(relacao, 2)])
    relacao = 0
    arq.close()
    capacidade_max = itens.pop(0)[1]
    while True:
        for i in range(len(itens)):
            if(relacao < itens[i][3] and itens[i][2] == 0):
                peso = itens[i][1]
                valor = itens[i][0]
                index = i
        if(capacidade_max > capacidade_atual + peso):
            itens[index][2] = 1
            capacidade_atual += peso
            valor_total += valor
        else:
            return [capacidade_max, capacidade_atual, valor_total, itens]
        relacao = 0


if __name__ == '__main__':
    resultado = Guloso2()
    print(resultado)
    peso = 0
    valor = 0
    for i in range(len(resultado[3])):
        if(resultado[3][i][2] == 1):
            peso += resultado[3][i][1]
            valor += resultado[3][i][0]
    print(peso)
    print(valor)
    for i in range(len(resultado[3])):
        if(resultado[3][i][2] == 1):
            print(resultado[3][i])