# Função 1: Abordagem de força bruta
def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):  # Comparar cada elemento com os outros
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

# Análise:
# - A complexidade de tempo dessa abordagem é O(n²), pois para cada elemento na lista
#   (loop externo), percorremos o restante da lista (loop interno).
# - A complexidade de espaço é O(d), onde d é o número de duplicados armazenados.

# Função 2: Utilizando uma estrutura de dados (conjunto)
def encontrar_duplicados_com_conjunto(lista):
    vistos = set()
    duplicados = set()
    for num in lista:
        if num in vistos:  # Se já vimos o número, é um duplicado
            duplicados.add(num)
        else:
            vistos.add(num)  # Caso contrário, adicionamos aos já vistos
    return list(duplicados)

# Análise:
# - A complexidade de tempo dessa abordagem é O(n), pois percorremos a lista uma única vez,
#   e as operações com conjuntos (adicionar e verificar) têm complexidade O(1) em média.
# - A complexidade de espaço é O(n), porque utilizamos memória extra para armazenar
#   os conjuntos de elementos vistos e duplicados.
