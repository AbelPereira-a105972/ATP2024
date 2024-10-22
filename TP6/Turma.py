def menu():
    print("""--------------- MENU ---------------
      (1) Criar nova turma
      (2) Inserir aluno
      (3) Editar aluno
      (4) Remover aluno
      (5) Listar turma
      (6) Consultar ID
      (7) Guardar turma
      (8) Carregar turma
      (0) Sair
          """)
    
def turmaVazia(nturma):
    cond = False
    if nturma == "":
        print("Adicione ou carregue uma turma antes de continuar.")
        cond = True
    return cond
    
def save(turma, nturma):
    cond = False
    if nturma == "":
        cond = True
    elif nturma != "":
        print("Têm progresso por guardar. Todos os dados serão removidos!")
        ans = input("Deseja continuar? (S/N)").upper()
        while ans != 'S' and ans != 'N':
            ans = input("Selicione S ou N").upper()
        if ans == 'S':
            turma.clear()
            cond = True
    return cond
    
def existealuno(turma, ID):
    cond = True
    for aluno in turma:
        nome, id, notas = aluno
        if ID == id:
            cond = False
    return cond 

def inseriralunoTurma(turma, nturma):
    notas = []
    nome = input("Insira o nome do aluno")
    id = input("Insira o ID").lower()
    if not existealuno(turma,id):
        print(f"O ID: {id} já se encontra registado na turma.\n")
    else:
        notatpc = int(input("Insira a nota do TPC"))
        notapr = int(input("Insira a nota do projeto"))
        notateste = int(input("Insira a nota do teste"))
        notas.append(notatpc)
        notas.append(notapr)
        notas.append(notateste)
        aluno = nome, id, notas
        turma.append(aluno)
        print(f"O aluno {nome} com ID:{id} foi inserido na turma {nturma}.\n")
    return

def editAluno(turma, ID, nturma):
    sel = '1'
    for aluno in turma:
        nome, id, notas = aluno
        if id == ID:
            turma.remove(aluno)
            while sel != '0':
                print("""
        (1) Nome
        (2) Notas
        (0) Sair
""")
                sel = input("Selecione o que pretende alterar")
                if sel == '1':
                    nome = input("Insira o nome do aluno")
                    print(f"Alteração efetuada: {nome}, {id}, {notas[0]}, {notas[1]}, {notas[2]}")
                elif sel == '2':
                    notas = []
                    notatpc = int(input("Insira a nota do TPC"))
                    notapr = int(input("Insira a nota do projeto"))
                    notateste = int(input("Insira a nota do teste"))
                    notas.append(notatpc)
                    notas.append(notapr)
                    notas.append(notateste)
                    aluno = nome, id, notas
                    turma.append(aluno)
                    print(f"Alteração efetuada: {nome}, {id}, {notas}")
    return

def removeAluno(turma, ID, nturma):
    cond = False
    for aluno in turma:
        nome, id, notas = aluno
        if id == ID:
            turma.remove(aluno)
            print(f"O aluno {nome} foi removido da turma {nturma}.\n")
            cond = True
    if not cond:
        print(f"ID {id} não existente.")

def listarTurma(turma, nturma):
    print(f"\n--------------------------Turma {nturma}--------------------------\n", end="")
    for aluno in turma:
        nome, id, notas = aluno
        print(f"{nome} ID: {id} Nota TPC: {notas[0]} Nota Projeto: {notas[1]} Nota Teste: {notas[2]}")
    print("")
    return 

def consultaraluno(turma,ID):
    cond = True
    for aluno in turma:
        nome, id, notas = aluno
        if ID == id:
            cond = False
            print(f"""
ID: {id}
Nome: {nome}
Notas: {notas}
""")
    if cond:
        print("Selecionou um ID inexistente.")
    return 

def guardar(turma, nturma):
    f = open(f"{nturma}.txt", "w")
    for aluno in turma:
        f.write(f"{aluno[0]}||{aluno[1]}||{aluno[2][0]}#{aluno[2][1]}#{aluno[2][2]}\n")
    f.close()
    print("Documento guardado.")
    return

def carregar(turma, nturma):
    f = open(f"{nturma}.txt", "r")
    for line in f:
        aturma = line.split("||")
        nota = aturma[2].split("#")
        notas = [int(nota[0]), int(nota[1]), int(nota[2])]
        nome = aturma[0]
        id = aturma[1]
        aluno = (nome, id, notas)
        turma.append(aluno)
    f.close()
    return turma

opcao = '1'
turma = []
nturma = ""
menu()
while opcao != '0':
    opcao = input("Selecione uma opção")
    if opcao == '1':
        if save(turma, nturma):
            nturma = input("Selecione o nome da turma")
            nturma = nturma.upper()
            print(f"Criada turma {nturma}.")
            menu()
    elif opcao == '2':
        if not turmaVazia(nturma):
            inseriralunoTurma(turma, nturma)
            menu()
    elif opcao == '3':
        if not turmaVazia(nturma):
            ID = input("Selecione o ID do aluno")
            editAluno(turma, ID, nturma)
    elif opcao == '4':
        if not turmaVazia(nturma):
            ID = input("Selecione o ID do aluno")
            removeAluno(turma, ID, nturma)
    elif opcao == '5':
        if not turmaVazia(nturma):
            listarTurma(turma, nturma)
            menu()
    elif opcao == '6':
        if not turmaVazia(nturma):
            ID = input("Selecione um ID").lower()
            consultaraluno(turma,ID)
            menu()
    elif opcao == '7':
        if not turmaVazia(nturma):
            guardar(turma, nturma)
            turma.clear()
            nturma = ""
    elif opcao == '8':
        nturma = input("Selecione a turma").upper()
        carregar(turma, nturma)

print("Volte Sempre!")
