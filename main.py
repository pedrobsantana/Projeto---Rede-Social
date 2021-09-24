import csv

#caminho_conexoes = 'C:\\Users\\Flávio Quirino\\Desktop\\Programação\\Curso Lets Code - Pi DS\\Projetos\\Estruturas de Dados\\Projeto-Rede-Social\\conexoes.csv'
#caminho_usuarios = 'C:\\Users\\Flávio Quirino\\Desktop\\Programação\\Curso Lets Code - Pi DS\\Projetos\\Estruturas de Dados\\Projeto-Rede-Social\\usuarios.csv'

reader_conexoes = csv.reader(open("conexoes.csv", 'r', encoding = 'utf-8'))
#reader_conexoes = open("conexoes.csv", 'r', encoding = 'utf-8')

reader_usuarios = csv.reader(open("usuarios.csv", 'r', encoding = 'utf-8'))
#reader_usuarios = open("usuarios.csv", 'r', encoding = 'utf-8')

class Grafo():
    def __init__(self):
        self.adjacencia = {}

    def adiciona(self, vertice):
        # Para adicionar um vertice, simplesmente criamos a chave dele dentro nosso dicionario de adjacencia
        self.adjacencia[vertice] = {}
    
    def conecta(self, origem, destino, peso = 1):
        # Acessamos nosso vertice e criamos uma chave para a conexao dele, atribuindo o valor como sendo o peso
        self.adjacencia[origem][destino] = peso

    def exibir_perfil(self, nome):
        
        # seguindo
        seguindo = 0
        for el in self.adjacencia[nome].keys():
            seguindo += 1

        # seguidores
        seguidores = []
        for el in self.adjacencia.items():
            for el1 in el[1].items():
                if nome in el1:
                    seguidores.append(el1) 

        print(f"O usuário {nome} segue {seguindo} usuários e tem {len(seguidores)} seguidores.\n")

    def story(self, nome):
        
        lista_amigos = list(self.adjacencia[nome].items())

        melhores_amigos = []
        amigos_comuns = []

        # Separando 'Amigos comuns' dos 'Melhores Amigos'
        for el in lista_amigos:
            if el[1] == '2':
                melhores_amigos.append(el[0])
            else:
                amigos_comuns.append(el[0])

        # Bubblesort para melhores amigos
        for i in range(len(melhores_amigos)):
            for j in range(len(melhores_amigos)):
                if melhores_amigos[j] > melhores_amigos[i]:
                    melhores_amigos[i], melhores_amigos[j] = melhores_amigos[j], melhores_amigos[i]

        #Bubblesort para amigos comuns
        for i in range(len(amigos_comuns)):
            for j in range(len(amigos_comuns)):
                if amigos_comuns[j] > amigos_comuns[i]:
                    amigos_comuns[i], amigos_comuns[j] = amigos_comuns[j], amigos_comuns[i]

        #juntar ambas listas
        lista_story = melhores_amigos + amigos_comuns
        
        print(f'Exibição de stories do usuário {nome}: {lista_story}\n')

    def top_influencers(self, k):
    
        num_seguidores = {}

        for usuario in self.adjacencia:
            count = 0
            for seguindo in self.adjacencia.items():
                for el in seguindo[1]:
                    if usuario in el:
                        count += 1

            num_seguidores[usuario] = count

        # print(num_seguidores)

        influencers = list(num_seguidores.items())

        # Bubblesort para ordernar top influencers
        for i in range(len(influencers)):
            for j in range(len(influencers)):
                if influencers[j][1] > influencers[i][1]:
                    influencers[i], influencers[j] = influencers[j], influencers[i]

        print(f'*** TOP {k} INFLUENCERS ***')
        for el in influencers[::-1][:k]:
            print(f'{el[0]}: {el[1]}')
            
    def busca_caminho_usuarios(self, nome1, nome2):
        fila = [nome1]
        visitados = []
        predecessor = {nome1: None}
        
        #enquanto tiver elementos na fila
        while len(fila) > 0:
            primeiro_elemento = fila[0]
            fila = fila[1:]
            visitados.append(primeiro_elemento)
            for adjacente in self.adjacencia[primeiro_elemento].keys():
                
                # se achou, monta o caminho
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
        return False
                        

def cria_grafo():
    g = Grafo()
    for linha in reader_usuarios:
        g.adiciona(linha[1])

    for linha in reader_conexoes:
        g.conecta(linha[0], linha[1], linha[2])

    return g

g = cria_grafo()

g.exibir_perfil("helena42")
g.story("helena42")
g.top_influencers(5)
g.busca_caminho_usuarios("miguel1", "maria_alice19")