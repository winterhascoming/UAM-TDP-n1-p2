from collections import OrderedDict

alunos = OrderedDict()
indice_alunos = OrderedDict()


def guardar_aluno():
    email, nome = input("digite o nome: "), input("digite o email: ")
    alunos[email] = {"email": email, "nome": nome, "id": len(alunos.keys())}
    indice_alunos[nome] = email


def pesquisar_por_nome(nome: str):
    try:
        email = indice_alunos[nome]
    except KeyError:
        print("aluno não cadastrado")
    else:
        alunos[email]


def pesquisar_por_email(email: str):
    try:
        aluno = alunos[email]
    except KeyError:
        print("aluno não cadastrado")
    else:
        print(aluno)


def atualizar_dados(ref: str, email: str, nome: str):
    try:
        alunos[ref]
    except KeyError:
        try:
            ref = indice_alunos[ref]
        except KeyError:
            print("aluno não existe")
    if nome:
        nome_antigo = alunos[ref]["nome"]
        alunos[ref]["nome"] = nome
        indice_alunos[nome] = indice_alunos.pop(nome_antigo)
    if email:
        alunos[email] = alunos.pop(ref)
        indice_alunos[alunos[email]["nome"]] = email


def listar_usuarios():
    for item in sorted(alunos.values(), key=lambda item: item["id"]):
        print(item)


guardar_aluno()
guardar_aluno()
pesquisar_por_nome("ana")