def criarlista(N):
    import random
    res = []
    for i in range(N):
        num = random.randint(0,100)
        res.append(num)
    return res
def criarlista2(N):
    res = []
    for i in range(N):
        res.append(int(input()))
    return res
def somaLista(N):
    res = 0
    for i in N:
        res = res + i
    return res
def mediaLista(lista):
    res = 0
    if len(lista) == 0:
        res = 0
    else:
        for i in lista:
            res = res + i
        res = res/len(lista)
    return res
def maiorLista(lista):
    res = lista[0]
    for i in lista[1:]:
        if i > res:
            res = i
    return res
def menorLista(lista):
    res = lista[0]
    for i in lista[1:]:
        if i < res:
            res = i
    return res
def ord(cres):
    cond = True
    i = 0
    while cond and i < len(cres) - 1:
        if cres[i] < cres[i + 1]:
            res = "Sim, está em ordem crescente."
        if cres[i] > cres[i + 1]:
            res = "Não está em ordem crescente."
            cond = False
        i = i + 1
    return res
def ordd(decres):
    cond = True
    i = 0
    while cond and i < len(decres) - 1:
        if decres[i] > decres[i + 1]:
            res = "Sim, está em ordem decrescente."
        if decres[i] < decres[i + 1]:
            res = "Não está em ordem decrescente."
            cond = False
        i = i + 1
    return res
def proc(N,lista):
    for i in range(len(lista)):
        if N == lista[i]:
            pos = i
        elif N not in lista:
            pos = -1
    return pos
def menu():
    print("\n------------MENU------------\n")
    print("1- Criar Lista Aleatória\n2- Criar Lista\n3- Soma\n4- Média\n5- Maior\n6- Menor\n7- Ordenar Crescente\n8- Ordenar Decrescente\n9- Procura Elemento\n\n0-sair\n")
    cond = True
    while cond:
        opcao = int(input(print("Selecione uma opção do menu.")))
        while opcao not in [0,1,2,3,4,5,6,7,8,9]:
            opcao = int(input("Selecione uma opção válida!"))
        if opcao == 1:
            numlist = criarlista(int(input("Quantos elementos terá a sua lista?")))
            print("Lista criada!\n",numlist)
        if opcao == 2:
            numlist = criarlista2(int(input("Quantos elementos terá a sua lista?")))
            print("Lista criada!\n",numlist)
        if opcao == 3:
            print(somaLista(numlist))
        if opcao == 4:
            print(mediaLista(numlist))
        if opcao == 5:
            print(maiorLista(numlist))
        if opcao == 6:
            print(menorLista(numlist))
        if opcao == 7:
            print(ord(numlist))
        if opcao == 8:
            print(ordd(numlist))  
        if opcao == 9:
            print(proc(int(input("Que valor procura?")),numlist))
        if opcao == 0:
            print("Obrigado!")
            print(numlist)
            cond = False
menu()
