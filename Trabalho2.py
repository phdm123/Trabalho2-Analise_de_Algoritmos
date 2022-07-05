import time as t

def Guloso1():
    itens = []
    capacidade_atual = 0
    menor_peso = 10e16
    valor = 0
    valor_total = 0
    index = 0
    with open("large_scale/knapPI_3_2000_1000_1") as arq: #Arquivo que será lido pelo algoritmo, caso queira ler outro, altere o nome do mesmo
        for linha in arq.readlines():
            valor = linha.strip().split(' ')[0]
            peso = linha.strip().split(' ')[1]
            if(int(peso) <= 0):
                continue
            itens.append([int(valor), int(peso), 0])
    arq.close()
    capacidade_max = itens.pop(0)[1]
    while True:
        for i in range(len(itens)):
            if(itens[i][1] < menor_peso and itens[i][2] == 0):
                menor_peso = itens[i][1]
                valor = itens[i][0]
                index = i
        if(capacidade_max >= capacidade_atual + menor_peso):
            itens[index][2] = 1
            capacidade_atual += menor_peso
            valor_total += valor
        else:
            return valor_total
        menor_peso = 10e16

def Guloso2():
    itens = []
    capacidade_atual = 0
    peso = 0
    valor = 0
    valor_total = 0
    index = 0
    with open("large_scale/knapPI_3_2000_1000_1") as arq: #Arquivo que será lido pelo algoritmo, caso queira ler outro, altere o nome do mesmo
        for linha in arq.readlines():
            valor = linha.strip().split(' ')[0]
            peso = linha.strip().split(' ')[1]
            if(int(peso) <= 0):
                continue
            relacao = int(valor)/int(peso)
            itens.append([int(valor), int(peso), 0, round(relacao, 2)])
    arq.close()
    relacao = 0
    vetor_aux = itens.pop(0)
    for j in range(vetor_aux[0]):
        for i in range(len(itens)):
            if(relacao < itens[i][3] and itens[i][2] == 0):
                relacao = itens[i][3]
                peso = itens[i][1]
                valor = itens[i][0]
                index = i
        if(vetor_aux[1] >= capacidade_atual + peso):
            itens[index][2] = 1
            capacidade_atual += peso
            valor_total += valor
        else:
            itens[index][2] = -1
        relacao = 0
    for i in range(vetor_aux[0]):
        if(itens[i][2] == -1):
            itens[i][2] = 0
    return valor_total

def Dinamico():
    itens = []
    wt = []
    val = []
    with open("large_scale/knapPI_3_2000_1000_1") as arq: #Arquivo que será lido pelo algoritmo, caso queira ler outro, altere o nome do mesmo
        for linha in arq.readlines():
            valor = linha.strip().split(' ')[0]
            peso = linha.strip().split(' ')[1]
            if(int(peso) <= 0):
                continue
            itens.append([int(valor), int(peso)])
    W = itens.pop(0)[1]
    n = len(itens)
    for i in range(len(itens)):
        wt.append(itens[i][1])
        val.append(itens[i][0])
    V = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i==0 or j==0:
                V[i][j] = 0   
            elif wt[i - 1] <= j:
                V[i][j] = max(val[i - 1] + V[i - 1][j - wt[i - 1]] , V[i-1][j])
            else:
                V[i][j] = V[i - 1][j]
    return V[n][W]

if __name__ == '__main__':
    print("1 - Algoritmo Guloso 1\n2 - Algoritmo Guloso 2\n3 - Algoritmo Dinamico\nObs: Cheque o nome dos arquivos lidos nas funções.")
    resposta = input()
    if(resposta == '1'):
        start = t.time()
        print(Guloso1())
        end = t.time()
        print("Tempo transcorrido: " + str(round(end - start, 2)) + " Segundos")
    elif(resposta == '2'):
        start = t.time()
        print(Guloso2())
        end = t.time()
        print("Tempo transcorrido: " + str(round(end - start, 2)) + " Segundos")
    elif(resposta == '3'):
        start = t.time()
        print(Dinamico())
        end = t.time()
        print("Tempo transcorrido: " + str(round(end - start, 2)) + " Segundos")
    else:
        print("Número incorreto.")