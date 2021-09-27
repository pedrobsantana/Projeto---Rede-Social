import csv

reader_conexoes = csv.reader(open("conexoes.csv", 'r', encoding = 'utf-8'))
reader_usuarios = csv.reader(open("usuarios.csv", 'r', encoding = 'utf-8'))

class Grafo():
    def __init__(self):
        self.adjacencia = {}
     
    def adiciona(self, vertice):
        '''
        Definição: Função para adicionar um vértice (adicionar um usuário) e 
        criar a chave do vértice dentro do nosso dicionário de adjacência.

        Parametro: vertice(username).
        '''
        self.adjacencia[vertice] = {}
    
        
    def conecta(self, origem, destino, peso = 1):
        '''
        Definição: Função para conectar os usuários, acessar nosso vértice e criar uma chave para a conexão dele, 
        atribuindo o valor como sendo o peso

        Parametro: origem(username primário), destino(username que irá receber a ligação), 
        peso(qual tipo de ligação entre eles, 1-Amigos Comuns / 2-Melhores Amigos).
        '''
        self.adjacencia[origem][destino] = peso

        
    def exibir_perfil(self, nome):
        '''
        Definição: Função para exibir quantas pessoas que o perfil está seguindo e quantos seguidores possui.

        Parametro: nome(username).
        '''
        # Seguindo
        seguindo = 0
        for elemento in self.adjacencia[nome].keys():
            seguindo += 1
        
        # Seguidores
        seguidores = []
        for elemento in self.adjacencia.items():
            for el in elemento[1].items():
                if nome in el:
                    seguidores.append(el) 

        print(f"O usuário {nome} tem {len(seguidores)} seguidores e segue {seguindo} usuários.\n")

      
    def stories(self, nome):
        '''
        Definição: Função para ordenar a lista de Stories, por ordem alfabética com melhores amigos primeiro e depois amigos comuns.

        Parametro: nome(username).
        '''
        lista_amigos = list(self.adjacencia[nome].items())

        melhores_amigos = []
        amigos_comuns = []

        # Separando 'Amigos comuns' dos 'Melhores Amigos'
        for amigo in lista_amigos:
            if amigo[1] == '2':
                melhores_amigos.append(amigo[0])
            else:
                amigos_comuns.append(amigo[0])

        # Bubblesort para Melhores Amigos
        for i in range(len(melhores_amigos)):
            for j in range(len(melhores_amigos)):
                if melhores_amigos[j] > melhores_amigos[i]:
                    melhores_amigos[i], melhores_amigos[j] = melhores_amigos[j], melhores_amigos[i]

        # Bubblesort para Amigos Comuns
        for i in range(len(amigos_comuns)):
            for j in range(len(amigos_comuns)):
                if amigos_comuns[j] > amigos_comuns[i]:
                    amigos_comuns[i], amigos_comuns[j] = amigos_comuns[j], amigos_comuns[i]

        # Juntar as listas
        lista_stories = melhores_amigos + amigos_comuns
        
        print(f'Exibição de stories do usuário {nome}: {lista_stories}\n')
   

    def top_influencers(self, k):
        '''
        Definição: Função para encontrar quem tem mais seguidores na rede, os Top Influencers.

        Parametro: k(Numero de quantos do ranking para ver).
        '''   
        num_seguidores = {}

        for usuario in self.adjacencia:
            count = 0
            for seguindo in self.adjacencia.items():
                for elemento in seguindo[1]:
                    if usuario == elemento:
                        count += 1

            num_seguidores[usuario] = count

        influencers = list(num_seguidores.items())

        # Bubblesort para ordernar top influencers
        for i in range(len(influencers)):
            for j in range(len(influencers)):
                if influencers[j][1] > influencers[i][1]:
                    influencers[i], influencers[j] = influencers[j], influencers[i]

        print(f'*** TOP {k} INFLUENCERS ***')
        for elemento in influencers[::-1][:k]:
            print(f'{elemento[0]}: {elemento[1]}')
    

    def busca_caminho_usuarios(self, nome1, nome2):
        '''
        Definição: Função para encontrar o caminho entre uma pessoa e outra na rede.

        Parametro: nome1(usuario primario), nome2(usuario)
        '''
        fila = [nome1]
        visitados = []
        predecessor = {nome1: None}
        
        # Enquanto tiver elementos na fila
        while len(fila) > 0:
            primeiro_elemento = fila[0]
            fila = fila[1:]
            visitados.append(primeiro_elemento)
            for adjacente in self.adjacencia[primeiro_elemento].keys():
                
                # Se achou, monta o caminho
                if adjacente == nome2:
                    pred = primeiro_elemento
                    caminho_invertido = [nome2]
                    while pred is not None:
                        caminho_invertido.append(pred)
                        pred = predecessor[pred]
                        
                    caminho = ""
                    for no in caminho_invertido[::-1]:
                        caminho += f"{no} -> "
                    return print(f"\nO caminho entre os usuários {nome1} e {nome2} é: {caminho[:-3]}")
                
                if adjacente not in fila and adjacente not in visitados:
                    predecessor[adjacente] = primeiro_elemento
                    fila.append(adjacente)
        return print(f"Não foi possivel encontrar um caminho entre {nome1} e {nome2}.")


def cria_grafo():
    g = Grafo()
    for linha in reader_usuarios:
        g.adiciona(linha[1])

    for linha in reader_conexoes:
        g.conecta(linha[0], linha[1], linha[2])

    return g

g = cria_grafo()
g.exibir_perfil("helena42")
g.stories("helena42")
g.top_influencers(5)
g.busca_caminho_usuarios("helena42", "isadora45")