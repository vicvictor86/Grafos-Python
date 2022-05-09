import os, timeit, time
import matplotlib.pyplot as plt

def calcular_tempo_brute_force_timeit(vertex_quantity):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd() +'/timeIt/' + "tempoBruteForce" + "Tamanho" + str(vertex_quantity) +'.txt'
    name_file1 = os.getcwd() +'/timeIt/' + "temposApenasNum"+ "BruteForce" + "Tamanho" + str(vertex_quantity) +'.txt'

    arquivo = open(name_file, operacao)
    arquivo1 = open(name_file1, operacao)

    #calculando o bruteForce()
    print('>>> calculando brute force com tamanho ' + str(vertex_quantity))
    tempo_brute_force = 0
    tempo_brute_force += timeit.timeit("grafo.bruteForce()", setup="from __main__ import grafo", number=1)
    arquivo.write("bruteForce " + ": "  + "{:.12f}".format(float(tempo_brute_force)) + ";"+ '\n')
    arquivo1.write("{:.12f}".format(float(tempo_brute_force))+'\n')
    print('bruteForce done.')

    arquivo.close()

def calcular_tempo_heuristic_timeit(vertex_quantity):
    '''calcular tempo de execucao'''

    operacao = 'w'

    name_file = os.getcwd() +'/timeIt/' + "tempoHeuristic" + "Tamanho" + str(vertex_quantity) +'.txt'
    name_file1 = os.getcwd() +'/timeIt/' + "temposApenasNum"+ "Heuristic" + "Tamanho" + str(vertex_quantity) +'.txt'

    arquivo = open(name_file, operacao)
    arquivo1 = open(name_file1, operacao)

    #calculando o bruteForce()
    print('>>> calculando heuristic com tamanho ' + str(vertex_quantity))
    tempo_heuristic = 0
    lista_coberturas = []
    tempo_heuristic += timeit.timeit("grafo.vertex_cover_degrees(grafo.lista_Vertices, {})".format(lista_coberturas), setup="from __main__ import grafo", number=1)
    arquivo.write("heuristic " + ": " + "{:.12f}".format(float(tempo_heuristic)) + ";"+ '\n')
    arquivo1.write("{:.12f}".format(float(tempo_heuristic))+'\n')
    print('heuristic done.')
    
    arquivo.close()

def gerar_grafico(alghoritm_value, alghoritm_classification, tipo, size):
    ''''''
    y_axis = alghoritm_value
    print(y_axis)
    x_axis = range(len(y_axis))
    width_n = 0.4
    bar_color = 'green'
    algoritmos = alghoritm_classification

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align='center')
    plt.ylabel('Tempo(s)')
    plt.xlabel('Algoritmos e tamanhos')
    plt.xticks(x_axis, algoritmos, rotation='horizontal')
    plt.title('Tempo de execução com algoritmo '+str(tipo))
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(os.getcwd() + '/_plot/tempos-' + str(tipo) + str(size) + '.png')
    print('>>> figura', str(tipo), '.png salva!')
    plt.close()

def get_valores_pro_grafico(tipo, vertex_quantity):
    ''''''
    archive_list = []
    size_list = vertex_quantity
    for size in size_list:
        archive_list.append(open(os.getcwd()+'/timeIt/temposApenasNum'+str(tipo)+"Tamanho"+str(size)+'.txt', 'r'))

    valores = []
    for archive in archive_list:
        valores.append(archive.read())
        archive.close()
    
    alghoritm_size = []
    for i in range(len(valores)):
        alghoritm_size.append(float(valores[i]))
    print('alghorithmValue = ', alghoritm_size)

    alghoritm_classification =[]
    for size in size_list:
        alghoritm_classification.append(f"{str(tipo)} {str(size)}")
    
    gerar_grafico(alghoritm_size, alghoritm_classification, tipo, size)

def mostrarResultados(tipo, tam):
    arquivo = open(os.getcwd()+'/timeIt/temposTimeit'+str(tam)+str(tipo)+'.txt', 'r')
    valores = arquivo.read()
    arquivo.close()
    print("\nAlgoritmo->caso->tempo(s)->n de comparacoes\n")
    print(valores)
