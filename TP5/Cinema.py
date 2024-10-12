def menu ():
    print("""
    ---------- Menu ----------
    (1) Nova Sala
    (2) Novo Filme
    (3) Filmes em Exebição
    (4) Disponibilidade
    (5) Verificar Lugar
    (6) Comprar Bilhete
    (0) Sair
    --------------------------
    """)

def existesala(cinema, nome):
    cond = False 
    for sala in cinema:
        nlugares, vendidos, filme, salanome = sala
        if nome == salanome:
            print("Já existe uma sala com esse nome!")
            cond = True
    return cond

def inserirsala(cinema, nome):
    if not existesala(cinema, nome):
        vendidos = []
        nlugares = int(input("Quantos lugares tem a nova sala?"))
        filme = ""
        salanome = nome
        sala = nlugares, vendidos, filme, salanome
        cinema.append(sala)
    return

def filmes(cinema, nome):
    for i,sala in enumerate(cinema):
        nlugares, vendidos, filme, salanome = sala
        if nome == salanome:
            filme = input("Insira o nome do filme.")
            cinema[i] = nlugares, vendidos, filme, salanome
    return 

def listar(cinema):
    for sala in cinema:
        nlugares, vendidos, filme, nomesala = sala
        print(filme)
    return

def listardisponibilidade(cinema):
    for sala in cinema:
        nlugares, vendidos, filme, nomesala = sala
        vagos = nlugares - len(vendidos)
        print(f"--------{nomesala}|{filme}|livres:{vagos}|ocupados:{len(vendidos)}--------")
    return 

def disponivel(cinema, afilme, lugar):
    cond = True
    for sala in cinema:
        nlugares, vendidos, filme, nomesala = sala
        if afilme == filme:
            if lugar in vendidos:
                cond = False
    return cond

def vendebilhete(cinema, filme, lugar):
    for sala in cinema:
        nlugares, vendidos, filme, nomesala = sala
        if disponivel(cinema, filme, lugar):
            vendidos.append(lugar)
    return

opcao = '1'
cinema = []
menu()
while opcao != '0':
    opcao = input("Selecione uma opcao")
    if opcao == '1':
        nome = input("Selecione o nome da sala.")
        inserirsala(cinema, nome)
    if opcao == '2':
        nome = input("Insira a sala.")
        filmes(cinema, nome)
    if opcao == '3':
        listar(cinema)
    if opcao == '4':
        listardisponibilidade(cinema)
    if opcao == '5':
        afilme = input("Insira o filme.")
        lugar = input("Insira o lugar.")
        print(disponivel(cinema, afilme, lugar))
    if opcao == '6':
        afilme = input("Insira o filme.")
        lugar = input("Insira o lugar.")
        vendebilhete(cinema, afilme, lugar)
