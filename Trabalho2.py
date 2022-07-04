def Guloso1():
    itens = []
    capacidade_atual = 0
    menor = 10e16
    valor = 0
    valor_total = 0
    index = 0
    with open("large_scale/knapPI_1_100_1000_1") as arq: #Arquivo que será lido pelo algoritmo, caso queira ler outro, altere o nome do mesmo
        for linha in arq.readlines():
            peso = linha.strip().split(' ')[0]
            valor = linha.strip().split(' ')[1]
            itens.append([int(peso), int(valor), 0])
    arq.close()
    itens.pop(-1)
    capacidade_max = itens.pop(0)[1]
    while True:
        for i in range(len(itens)):
            if(itens[i][1] < menor and itens[i][2] == 0):
                menor = itens[i][1]
                valor = itens[i][0]
                index = i
        if(capacidade_max > capacidade_atual + menor):
            itens[index][2] = 1
            capacidade_atual += menor
            valor_total += valor
        else:
            return [capacidade_max, capacidade_atual, valor_total, itens]
        menor = 10e16

def Guloso2():
    ...

if __name__ == '__main__':
    resultado = Guloso1()
    print(resultado)