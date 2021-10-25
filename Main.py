from collections import OrderedDict

alunos = OrderedDict()
indice_alunos = OrderedDict()

def guardar_aluno():
    email, nome = input("Digite o email a ser cadastrado: "), input("Digite o Nome Completo a ser cadastrado: ")
    alunos[email] = {"email": email, "nome": nome, "id": len(alunos.keys())}
    indice_alunos[nome] = email


def pesquisar_por_nome(nome: str):
    try:
        email = indice_alunos[nome]
        print('Usuário encontrado no Sistema.')
    except KeyError:
        print("Usuário não encontrado no Sistema.")
    else:
        alunos[email]

def pesquisar_por_email(email: str):
    try:
        aluno = alunos[email]
        print('Usuário encontrado no Sistema.')
    except KeyError:
        print('Usuário não encontrado no Sistema.')
    else:
        print(aluno)

def atualizar_dados(ref: str, email: str, nome: str):
    try:
        alunos[ref]
    except KeyError:
        try:
            ref = indice_alunos[ref]
        except KeyError:
            print("O aluno não existe!")
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

def listar_usuarios_az():
    for alunos_az in sorted(alunos.values(), key=lambda item: item["nome"]):
        print(alunos_az)

def Menu(Escolha):
    while Escolha != 7:
        print('''        [ 1 ] Cadastrar Usuário
        [ 2 ] Exibir Cadastros
        [ 3 ] Exibir Cadastros A -> Z
        [ 4 ] Buscar Usuário
        [ 5 ] Excluir Usuário
        [ 6 ] Editar Cadastro
        [ 7 ] Encerrar Sistema''')
        Escolha = int(input('>>>'))
        if Escolha == 1:
            guardar_aluno()
        elif Escolha == 2:
            listar_usuarios()
        elif Escolha == 3:
            listar_usuarios_az()
        elif Escolha == 4:
            busca = input("Busca no Sistema pelo Usuário(Nome): ")
            pesquisar_por_nome(busca)
        elif Escolha == 5:
            pass
        elif Escolha == 6:
            atualizar_dados()
        elif Escolha == 7:
            print('Encerrando Sistema...')
        else:
            print('Escolha inválida. Tente novamente!')
        print('-=' * 25)

def main():
    Escolha = 0
    Menu(Escolha)

if __name__ == "__main__":
    main()
