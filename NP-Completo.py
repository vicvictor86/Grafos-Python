from Grafo import Grafo
from tempos import calcular_tempo_brute_force_timeit, calcular_tempo_heuristic_timeit, get_valores_pro_grafico

grafo = Grafo()

quantity_vertex = [5,6,7,10]

for quantity in quantity_vertex:
    grafo.create_random_graph(quantity)
    calcular_tempo_brute_force_timeit(len(grafo.lista_Vertices))
    calcular_tempo_heuristic_timeit(len(grafo.lista_Vertices))

get_valores_pro_grafico("Heuristic", quantity_vertex)
get_valores_pro_grafico("BruteForce", quantity_vertex)

solution = grafo.bruteForce()
for item in solution: # n
    solution_vertices = [] # 1
    adjacents = [] # 1
    count = 0 # 1
    k = len(item) # 1

    for vertice in item: # n
        solution_vertices.append(vertice.getId()) # 1
        adjacents = grafo.busca_Adjacentes(vertice) # n
        for adjacent in adjacents: # n
            grafo.remove_Aresta(vertice.getId(), adjacent.getId()) # n
        count += 1 #1

    if count == k and len(grafo.lista_Arestas) == 0: #1
        print(f"A solução {solution_vertices} gerada pelo algoritmo, é realmente uma solução para o problema de cobertura de vértices.")
    else:
        print(f"A solução {solution_vertices} gerada pelo algoritmo, não é uma solução para o problema de cobertura de vértices.")
