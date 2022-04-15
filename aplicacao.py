from Grafo import Grafo
from copy import deepcopy

option = 1
grafo = Grafo()
grafo_exemplo = Grafo()

grafo_exemplo.novo_Vertice(1)
grafo_exemplo.novo_Vertice(2)
grafo_exemplo.novo_Vertice(3)
grafo_exemplo.novo_Vertice(4)
grafo_exemplo.novo_Vertice(5)
grafo_exemplo.novo_Vertice(6)

grafo_exemplo.nova_Aresta(1, 2, 0)
grafo_exemplo.nova_Aresta(1, 3, 0)
grafo_exemplo.nova_Aresta(2, 3, 0)
grafo_exemplo.nova_Aresta(2, 4, 0)
grafo_exemplo.nova_Aresta(3, 5, 0)
grafo_exemplo.nova_Aresta(4, 6, 0)
grafo_exemplo.nova_Aresta(4, 5, 0)

while option:
    print("Vértice-Local de câmera\nAresta-Corredor\n\nOpções:\n1-Adicionar local de câmera\n2-Adicionar um corredor\n3-Remover local de câmera\n4-Remover um corredor",
        "\n5-Utilizar exemplo\n6-Realizar Cobertura Mínima de Vértices\n7-Realizar cobertura heurística\n8-Mostrar Grafo\n0-Sair da Aplicação\n")
    option = int(input("O que deseja fazer ? "))

    if option == 1:
        v = int(input("Digite o numero correspondente ao vértice que representa este local: "))
        if not grafo.novo_Vertice(v):
            print("Selecione outro numero, esse vértice ja existe.")
        else:
            print("Local de câmera {} adicionado com sucesso.".format(v))
    elif option == 2:
        v = int(input("Digite o numero correspondente ao primeiro local: "))
        w = int(input("Digite o numero correspondente ao segundo local: "))
        if grafo.nova_Aresta(v, w, 0):
            print("Corredor {}-{} adicionado com sucesso.".format(v, w))
        else:
            print("Não foi possível adicionar o corredor. Verifique o índice dos vértices.")
    elif option == 3:
        v = int(input("Digite o numero correspondente ao local: "))
        if grafo.novo_Vertice(v) is None:
            print("Não existe local com esse identificador.")
        else:
            grafo.remove_vertice(v)
    elif option == 4:
        v = int(input("Digite o numero correspondente ao primeiro local de câmera do corredor: "))
        w = int(input("Digite o numero correspondente ao segundo local do corredor: "))
        if not grafo.remove_Aresta(v, w):
            print("Não existe corredor com esses locais de câmera.")
        else:
            grafo.remove_Aresta(v, w)
            print("Corredor {}-{} removido com sucesso.".format(v, w))
    elif option == 5:
        grafo = deepcopy(grafo_exemplo)
        print("Grafo alterado para o grafo exemplo")
    elif option == 6:
        for item in grafo_exemplo.bruteForce():
            for vertice in item:
                print(vertice.getId(), end=" ")
            print()
    elif option == 7:
        lista_coberturas = []
        grafo.vertex_cover_degrees(grafo.lista_Vertices, lista_coberturas)
        for item in lista_coberturas:
            for vertice in item:
                print(vertice, end=" ")
            print()
    elif option == 8:
        print(grafo.printa_grafo())
