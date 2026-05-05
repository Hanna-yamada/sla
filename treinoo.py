# importando o jogador 
from classes import Jogador
# importando a Equipe
from classes import Equipe
# lista dos jogadores
lista_j = []
# lista das equipes
lista_e = []
opcao = 1
# tratamento de erros

    # Codigo sai do loop ao usuario digitar 0
while opcao != 0:
    try:
        print("MENU")
        print("1 - Cadastrar Jogadores")
        print("2 - Cadastrar equipe")
        print("3 - Adicionar jogador a uma equipe")
        print("4 - Listar todas as equipes")
        print("5 - Listar jogadores de uma equipe")
        print("6 - Buscar jogador por nickname")
        print("0 - Sair")

        # Usuario digita uma opção
        opcao = int(input("Escolha uma opção: "))

        # Codigo Cadastrar jogador 
        if opcao == 1:
            # vf usado pra dizer se jogador já cadastrado
            vf = False
            # criando o objeto jogador e seus atributos
            jg = Jogador()
            jg.nome_jogador = input("Digite o nome do jogador: ")
            # for que verifica se jogador já está cadastrado
            for veri in lista_j:
                if(jg.nome_jogador == veri.nome_jogador):
                    vf = True
            
            # caso o jogador não estiver cadastrado
            if not vf:
                jg.nick = input("Digite o nick do jogador: ")
                jg.apelido = input("Digite o apelido do jogador: ")
                jg.cadastro_jogadores()
                lista_j.append(jg)

            # caso o jogador já estiver cadastrado
            else:
                print("Jogador já se encontra cadastrado")
        
        # Codigo cadastrar Equipe 
        elif opcao == 2:
            # vf usado para verificar se a equipe ja está cadastrada
            vf = False
            # criando o objeto equipe e seus atributos
            eq = Equipe()
            eq.nome_equipe = input("Digite o nome da equipe: ")
            # veri usado para verificar se a equipe já esta no sistema 
            for veri in lista_e:
                if(eq.nome_equipe == veri.nome_equipe):
                    vf = True
                    break
            # se equipe não cadastrada 
            if not vf:
                eq.jogo = input("Digite o nome do jogo da equipe: ")
                eq.cadastro_equipe()
                lista_e.append(eq)
            #  se a equipe já tiver cadastrada
            else:
                print("Equipe já se encontra Cadastrada")

        # add jogador a uma equipe
        elif opcao == 3:
            # vf se jogador 
            vf = False
            vf2 = False
            print("Lista de Jogadores Disponiveis")
            for a in lista_j:
                print(f"Jogadores: {a.nome_jogador} disponivel ")
            print("Lista de Equipes Disponiveis")
            for b in lista_e:
                print(f"Equipes: {b.nome_equipe} disponivel ")
            
            jogadores = input("Digite o nome do Jogador: ")
            for c in lista_j:
                if(jogadores == c.nome_jogador):
                    nome_equipe = input("Digite o nome da equipe: ")
                    vf = True
                    for d in lista_e:
                        if(nome_equipe == d.nome_equipe):
                            d.adicionar_jogador(c)
                            vf2 = True
                            break
                    break

            if not vf:
                print("Jogador não encontrado")
            elif not vf2:
                    print("Equipe não encontrada") 
                 
        # Codigo pra listar as equipes
        elif opcao == 4:
            # Laco for pra percorrer os nomes da equipe e executar o def
            for e in lista_e:
                e.listar_equipes()

        # Codigo para olhar os ingrantes da equipe
        elif opcao == 5:

            # vf usado para verificar se a equipe está na lista
            vf = False
            nome = input("Digite o nome da equipe: ")
            # percorre a lista das equipes
            for v in lista_e:
                # se a equipe estiver na lista roda o def e para a repetição
                if(nome == v.nome_equipe):
                    v.consultar_equipes()
                    vf = True
                    break
            # caso a equipe não for encontrada
            if not vf:
                print("Equipe não encontrada") 

        # Codigo do nick
        elif opcao == 6:
            # vf usado para verificar se o jogador está na lista
            vf = False
            nick = input("Digite o Nick do jogador: ")
            # percorre a lista dos jogadores
            for q in lista_j:
                # se o nick estiver na lista roda o def e para a repetição
                if nick == q.nick:
                    q.procurar_nick()
                    vf = True
                    break
            # se não escontrar jogador 
            # not inverte false = true / true = false
            if not vf:
                print("Nick do jogador não encontrado")

        # sai do loop
        elif opcao == 0:
            print("Saindo....")

        # caso o usuario digitar um numero que não está no menu
        else:
            print("Digite um numero de 1 a 6")

# mostra o que deu erro e printa pro usuario
    except Exception as erro:
        print(f"Deu erro {erro}")