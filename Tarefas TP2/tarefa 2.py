
# Função para ordenar a lista de registros
def ordenar_lista(lista):
    # Utiliza o Timsort, implementado na função sorted() do Python
    return sorted(lista)

# Análise:
# - O Timsort é o algoritmo de ordenação usado pela função sorted() no Python.
# - É um algoritmo eficiente e estável, baseado em Merge Sort e Insertion Sort.
# - No pior caso, sua complexidade de tempo é O(n log n), onde n é o tamanho da lista.
# - A complexidade de espaço no pior caso é O(n), devido ao uso de memória auxiliar.