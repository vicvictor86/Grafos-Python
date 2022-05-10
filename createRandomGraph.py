from Grafo import Grafo
from tempos import calcular_tempo_brute_force_timeit, calcular_tempo_heuristic_timeit, get_valores_pro_grafico

def calcula_tempo_grafos_aleatorios():
    quantity_vertex = [5, 10, 15]
    for quantity in quantity_vertex:
        grafo = Grafo()
        grafo.create_random_graph(quantity)
        calcular_tempo_brute_force_timeit(len(grafo.lista_Vertices))
        calcular_tempo_heuristic_timeit(len(grafo.lista_Vertices))

    get_valores_pro_grafico("Heuristic", quantity_vertex)
    get_valores_pro_grafico("BruteForce", quantity_vertex)