# classe jogador
class Jogador:
    def __init__ (self):
        self.nome_jogador = ""
        self.nick = ""
        self.apelido = ""

    def cadastro_jogadores (self):
        print(f"Jogador {self.nome_jogador}: adicionado")


    def procurar_nick (self):
            print(f"Nome do Jogador: {self.nome_jogador} / Nick: {self.nick} / Apelido: {self.apelido}")

class Equipe:
    def __init__ (self):
        self.nome_equipe = ""
        self.jogo = ""
        self.jogadores = [] 


    def cadastro_equipe (self):
        print(f"Equipe: {self.nome_equipe} adicionado")


    def adicionar_jogador(self,jogador):
        self.jogadores.append(jogador)
        print(f"Jogador: {jogador.nome_jogador} adicionado na equipe: {self.nome_equipe}")


    def listar_equipes (self):
              print(f"Equipe: {self.nome_equipe}  Jogo: {self.jogo}  Nº Jogadores: {len(self.jogadores)} ")

    def consultar_equipes(self):
        if len(self.jogadores) == 0:
            print("Nenhum jogador na equipe.")
        else:
            for j in self.jogadores:
                print(f"Nome: {j.nome_jogador} / Nick: {j.nick} / Apelido: {j.apelido}")