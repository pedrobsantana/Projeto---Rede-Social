import csv

caminho_conexoes = 'C:\\Users\\Flávio Quirino\\Desktop\\Programação\\Curso Lets Code - Pi DS\\Projetos\\Estruturas de Dados\\Projeto-Rede-Social\\conexoes.csv'
caminho_usuarios = 'C:\\Users\\Flávio Quirino\\Desktop\\Programação\\Curso Lets Code - Pi DS\\Projetos\\Estruturas de Dados\\Projeto-Rede-Social\\usuarios.csv'

df_conexoes = open(caminho_conexoes, 'r', encoding = 'utf-8')
reader_conexoes = csv.reader(df_conexoes)
df_usuarios = open(caminho_usuarios, 'r', encoding = 'utf-8')
reader_usuarios = csv.reader(df_usuarios)
class Grafo():
    def __init__(self):
        self.adjacencia = {}

    def adiciona(self, vertice):
        # Para adicionar um vertice, simplesmente criamos a chave dele dentro nosso dicionario de adjacencia
        self.adjacencia[vertice] = {}
    
    def conecta(self, origem, destino, peso = 1):
        # Acessamos nosso vertice e criamos uma chave para a conexao dele, atribuindo o valor como sendo o peso
        self.adjacencia[origem][destino] = peso

def cria_grafo():
    g = Grafo()
    for linha in reader_usuarios:
        g.adiciona(linha[1])

    for linha in reader_conexoes:
        g.conecta(linha[0], linha[1], linha[2])

    return g

g = cria_grafo()


def exibir_perfil(nome):
    # seguindo ****** verificar se precisa fazer validação de entrada (sting)
    seguindo = 0
    for el in g.adjacencia[nome].keys():
        seguindo += 1

    print(f'seguindo: {seguindo}.\n')

    # seguidores
    seguidores = 0
    for el in g.adjacencia.keys():
        if nome == g.adjacencia[el].keys():
            seguindo += 1

    print(f'seguidores: {seguidores}.\n')

exibir_perfil('helena42')

print(g.adjacencia['helena42'].items())
