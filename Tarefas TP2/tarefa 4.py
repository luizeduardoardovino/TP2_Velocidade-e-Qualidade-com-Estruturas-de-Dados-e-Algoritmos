# Função para ordenar uma pilha em ordem crescente
def ordenar_pilha(pilha):
    # Criar uma pilha auxiliar vazia
    pilha_aux = []
    
    # Enquanto a pilha original não estiver vazia
    while pilha:
        # Remover o elemento do topo da pilha original
        topo = pilha.pop()
        
        # Enquanto a pilha auxiliar não estiver vazia e o topo da pilha auxiliar for maior que o elemento atual
        while pilha_aux and pilha_aux[-1] > topo:
            # Mover o elemento da pilha auxiliar de volta para a pilha original
            pilha.append(pilha_aux.pop())
        
        # Inserir o elemento na pilha auxiliar
        pilha_aux.append(topo)
    
    # Mover os elementos de volta para a pilha original (opcional, dependendo do formato desejado)
    while pilha_aux:
        pilha.append(pilha_aux.pop())
    
    return pilha

# Exemplo de uso
pilha = [4, 2, 3, 1, 5]
print("Pilha original:", pilha)
ordenar_pilha(pilha)
print("Pilha ordenada:", pilha)

# Análise:
# - A complexidade de tempo no pior caso é O(n²), pois para cada elemento da pilha original
#   pode ser necessário percorrer toda a pilha auxiliar.
# - A complexidade de espaço é O(n), pois utilizamos uma pilha auxiliar com, no máximo, o mesmo número de elementos da pilha original.
