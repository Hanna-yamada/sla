from peewee import *

banco = SqliteDatabase("agenda.db")


class Contato(Model):
    nome = CharField()
    telefone = CharField(unique=True)
    data_cadastro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = banco
        table_name = "contatos"

    def __str__(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M:%S")
        return f"ID: {self.id} | Nome: {self.nome} | Telefone: {self.telefone} | Cadastro: {data_formatada}"


def criar_tabelas():
    banco.connect()
    banco.create_tables([Contato], safe=True)


def popular_contatos_iniciais():
    if not Contato.select().exists():
        contatos = [
            {"nome": "Ana Silva", "telefone": "11999990001"},
            {"nome": "Bruno Costa", "telefone": "11999990002"},
            {"nome": "Carla Mendes", "telefone": "11999990003"},
        ]
        for dados in contatos:
            Contato.create(**dados)
        print("Banco inicializado com 3 contatos de teste.")


def cadastrar_contato():
    print("\n===== CADASTRAR CONTATO =====")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()

    if not nome or not telefone:
        print("Nome e telefone são obrigatórios.")
        return

    try:
        contato = Contato.create(nome=nome, telefone=telefone)
        print("\nContato cadastrado com sucesso!")
        print(contato)
    except IntegrityError:
        print("Erro: já existe um contato com esse telefone.")


def listar_contatos():
    print("\n===== TODOS OS CONTATOS =====")
    contatos = Contato.select().order_by(Contato.id)

    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    for contato in contatos:
        print(contato)


def buscar_contato_por_nome():
    print("\n===== BUSCAR CONTATO POR NOME =====")
    termo = input("Digite nome ou parte do nome: ").strip()

    if not termo:
        print("Termo de busca inválido.")
        return

    contatos = Contato.select().where(Contato.nome.contains(termo)).order_by(Contato.nome)

    if not contatos:
        print("Nenhum contato encontrado.")
        return

    for contato in contatos:
        print(contato)


def editar_contato_por_id():
    print("\n===== EDITAR CONTATO =====")
    try:
        id_contato = int(input("Digite o ID do contato: "))
    except ValueError:
        print("ID inválido. Digite um número.")
        return

    contato = Contato.get_or_none(Contato.id == id_contato)

    if contato is None:
        print("Contato não encontrado.")
        return

    novo_nome = input(f"Novo nome ({contato.nome}): ").strip()
    novo_telefone = input(f"Novo telefone ({contato.telefone}): ").strip()

    if novo_nome:
        contato.nome = novo_nome
    if novo_telefone:
        contato.telefone = novo_telefone

    try:
        contato.save()
        print("Contato atualizado com sucesso!")
        print(contato)
    except IntegrityError:
        print("Erro: esse telefone já está em uso por outro contato.")


def excluir_contato_por_id():
    print("\n===== EXCLUIR CONTATO =====")
    try:
        id_contato = int(input("Digite o ID do contato: "))
    except ValueError:
        print("ID inválido. Digite um número.")
        return

    contato = Contato.get_or_none(Contato.id == id_contato)

    if contato is None:
        print("Contato não encontrado.")
        return

    confirmacao = input(f"Deseja excluir {contato.nome}? (s/n): ").strip().lower()

    if confirmacao not in ("s", "sim", "y", "yes"):
        print("Exclusão cancelada.")
        return

    contato.delete_instance()
    print("Contato excluído com sucesso.")


def mostrar_menu():
    print("\n===== AGENDA DE CONTATOS =====")
    print("1 - Cadastrar contato")
    print("2 - Ver todos os contatos")
    print("3 - Buscar contato pelo nome")
    print("4 - Editar contato pelo ID")
    print("5 - Excluir contato pelo ID")
    print("6 - Sair")


def main():
    criar_tabelas()
    popular_contatos_iniciais()

    while True:
        mostrar_menu()
        try:
            opcao = input("Escolha uma opção: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma encerrado.")
            break

        if opcao == "1":
            cadastrar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato_por_nome()
        elif opcao == "4":
            editar_contato_por_id()
        elif opcao == "5":
            excluir_contato_por_id()
        elif opcao == "6":
            print("\nAté logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

    banco.close()


if __name__ == "__main__":
    main()
