import pandas as pd

df_conexoes = pd.read_csv('conexoes.csv', encoding = 'utf-8')
df_usuarios = pd.read_csv('usuarios.csv', encoding = 'utf-8')

df_conexoes.head()
class Grafo():
    def __init__(self):
        self.adjacencia = {}

    def adiciona(self, vertice):
        # Para adicionar um vertice, simplesmente criamos a chave dele dentro nosso dicionario de adjacencia
        self.adjacencia[vertice] = {}
    
    def conecta(self, origem, destino, peso = 1):
        # Acessamos nosso vertice e criamos uma chave para a conexao dele, atribuindo o valor como sendo o peso
        self.adjacencia[origem][destino] = peso
        self.adjacencia[destino][origem] = peso


