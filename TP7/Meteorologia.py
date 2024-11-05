import matplotlib.pyplot as plt

def menu():
    print("""--------------- MENU ---------------
          
    (1) Criar/Editar Tabela
    (2) Guardar ficheiro
    (3) Carregar ficheiro
    (4) Dados térmicos 
    (5) Análises 
    (6) Gráficos 
    (0) Sair
          """)

def menu2():
    print("""
    (1) Média
    (2) Temperatura mínima
    (3) Temperatura máxima
    (4) Máxima precipitação
    (5) Amplitude térmica
    (0) Voltar ao menu
          """)
    
def menu3():
    print("""
    (1) Dias com precipitação inferior
    (2) Número de dias com precipitação superior
    (0) Voltar ao menu
          """)
    
def menu4():
    print("""
    (1) Gráfico da temperatura mínima e máxima
    (2) Gráfica da pluviosidade
    (0) Voltar ao menu
          """)

def criar(tabMeteo):
    cond = True
    print("Escolha uma data existente para alterar ou crie uma nova data.")
    print("Insira a data (AAAA/MM/DD)\n")
    ano = int(input("Ano?"))
    mes = int(input("Mês?"))
    dia = int(input("Dia?"))
    datan = (ano,mes,dia)
    if tabMeteo != []:
        for d in tabMeteo:
            data,*_ = d
            if datan == data and cond:
                print("A data que selecionou já se encontra no sistema. Deseja substituir? (S/N)")
                cond = False
                resp = input("").upper()
                if resp == 'S':
                    tabMeteo.remove(d)
    if cond or resp == 'S':
        tempm = float(input("Introduza a temperatura mínima"))
        tempM = float(input("Introduza a temperatura máxima"))
        prec = float(input("Introduza a percipitação"))
        tabMeteo.append((datan,tempm,tempM,prec))
        print("Dia inserido com sucesso.\n")
    return tabMeteo

def guardaTabMeteo(t, fnome):
    f = open(f"{fnome}.txt", "w")
    for data, min, max, prec in t:
        ano, mes, dia = data
        registo = f"{ano}-{mes}-{dia}|{min}|{max}|{prec}\n"
        f.write(registo)
    f.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(f"{fnome}.txt", "r")
    for line in file:
        line = line.strip()
        campos = line.split("|")
        data, min, max, prec = campos
        ano, mes, dia = data.split("-")
        tuplo = ((int(ano), int(mes), int(dia)), float(min), float(max), float(prec))
        res.append(tuplo)
    file.close()
    return res

def medias(tabMeteo):
    res = []
    print("Dia:                     Temperatura média:")
    for data,min,max,_ in tabMeteo:
        media = (min+max)/2
        res.append((data, media))
        print(f"{data[0]}/{data[1]}/{data[2]}                      {media}ºC")
    return 

def mintab(tabMeteo):
    minima = tabMeteo[0][1]
    datan = tabMeteo[0][0]
    for data, min, *_ in tabMeteo[1:]:    
        if minima > min:
            datan = data
            minima = min
    return f"A temperatura mínima foi de {minima} em {datan[0]}/{datan[1]}/{datan[2]}."

def maxtab(tabMeteo):
    maximo = tabMeteo[0][2]
    datan = tabMeteo[0][0]
    for data, _, max,_ in tabMeteo[1:]:   
        if max > maximo:
            datan = data
            maximo = max
    return f"A temperatura máxima foi de {maximo} em {datan[0]}/{datan[1]}/{datan[2]}."

def maxprec(tabMeteo):
    max_prec = tabMeteo[0][3]
    for data,_,_, prec in tabMeteo[1:]:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return f"A máxima precipitação foi de {max_prec} em {max_data[0]}/{max_data[1]}/{max_data[2]}."

def amplTerm(tabMeteo):
    res = []
    print("Dia:                     Amplitude térmica:")
    for data, min, max,_ in tabMeteo:
        amp = max - min
        tuplo = (data, amp)
        res.append(tuplo)
        print(f"{data[0]}/{data[1]}/{data[2]}                      {amp}ºC")
    return 

def diasChuvosos(tabMeteo, p):
    res = []
    print(f"""Dias com precipitação superior a {p}
Dia:                                 Precipitação:
        """)
    for data,_,_,prec in tabMeteo:
        if prec > p:
            res.append((data,prec))
            print(f"{data[0]}/{data[1]}/{data[2]}                                {prec}")
    return

def maxPeriodoCalor(tabMeteo, p):
    maior = 0 
    i = 0 
    for _,_,_, prec in tabMeteo:
        if prec < p:
            i = i + 1
        else:
            if i > maior:
                maior = i
            i = 0
    if i > maior:
                maior = i
    return f"A maior vaga de dias com precipitação abaixo de {p} foi de {maior} dia(s)."

def grafTabMeteot(tabMeteo):
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data,*_ in tabMeteo]
    temps_min = [min for _,min,*_ in tabMeteo]
    temps_max = [man for _,_,man,*_ in tabMeteo]

    plt.plot(datas,temps_min, label = "Temp Mínima", color = "g", marker = "o")
    plt.plot(datas,temps_max, label = "Temp Máxima", color = "r", marker = "o")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura mínima")
    plt.legend()
    plt.show()
    return 

def grafTabMeteop(tabMeteo):
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data,*_ in tabMeteo]
    precs = [prec for _,_,_,prec in tabMeteo]

    plt.bar(datas, precs, color = "Blue")
    plt.xlabel("Data")
    plt.ylabel("Pluviosidade mm")
    plt.title("Precipitação")
    plt.show()
    return 

def ficheiro(fnome):
    cond = False
    if fnome == "":
        print("Carregue um ficheiro antes de continuar")
        cond = True
    return cond

tabMeteo = []
fnome = ""
op = 'm'
menu()
while op != '0':
    op = input("Selecione uma opção")
    if op == '1':
        criar(tabMeteo)
        menu()
    elif op == '2':
        guardaTabMeteo(tabMeteo, fnome)
        print("Ficheiro guardado com sucesso.")
    elif op == '3':
        fnome = input("Insira o nome do ficheiro")
        tabMeteo = carregaTabMeteo(fnome)
        print("Ficheiro carregado com sucesso.")
    elif op == '4':
        if not ficheiro(fnome):
            menu2()
            op2 = 'm'
            while op2 != '0':
                op2 = input("")
                if op2 == '1':
                    medias(tabMeteo)
                elif op2 == '2':
                    print(mintab(tabMeteo))
                elif op2 == '3':
                    print(maxtab(tabMeteo))
                elif op2 == '4':
                    print(maxprec(tabMeteo))
                elif op2 == '5':
                    amplTerm(tabMeteo)
        menu()
    elif op == '5':
        if not ficheiro(fnome):
            menu3()
            op3 = 'm'
            while op3 != '0':
                op3 = input("")
                if op3 == '1':
                    lim = float(input("Selecione o valor de referência"))
                    diasChuvosos(tabMeteo, lim)
                if op3 == '2':
                    lim = float(input("Selecione o valor de referência"))
                    print(maxPeriodoCalor(tabMeteo, lim))
        menu()
    elif op == '6':
        if not ficheiro(fnome):
            menu4()
            op4 = 'm'
            while op4 != '0':
                op4 = input("")
                if op4 == '1':
                    grafTabMeteot(tabMeteo)
                if op4 == '2':
                    grafTabMeteop(tabMeteo)
        menu()

print("Volte Sempre!")
