def testaResultadoEmTempoPolinomial(grafo):
    solution = grafo.bruteForce()
    for item in solution: 
        solution_vertices = [] 
        adjacents = [] 
        count = 0 
        k = len(item) 

        for vertice in item: 
            solution_vertices.append(vertice.getId()) 
            adjacents = grafo.busca_Adjacentes(vertice) 
            for adjacent in adjacents: 
                grafo.remove_Aresta(vertice.getId(), adjacent.getId()) 
            count += 1 

        if count == k and len(grafo.lista_Arestas) == 0: 
            print(f"A solução {solution_vertices} gerada pelo algoritmo, é realmente uma solução para o problema de cobertura de vértices.")
        else:
            print(f"A solução {solution_vertices} gerada pelo algoritmo, não é uma solução para o problema de cobertura de vértices.")
