# Função para exibir a próxima tarefa na pilha
def tarefa_no_topo(pilha_de_tarefas):
    if not pilha_de_tarefas:
        return "A pilha de tarefas está vazia."  # Retorna uma mensagem se a pilha estiver vazia
    return pilha_de_tarefas[-1]  # Retorna o último elemento da lista, que é o topo da pilha

# Exemplo de uso
pilha_de_tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]  # Tarefa 3 está no topo
print("Próxima tarefa:", tarefa_no_topo(pilha_de_tarefas))

# Análise:
# - A operação de acessar o último elemento de uma lista em Python é O(1),
#   já que estamos apenas acessando o índice final sem realizar loops ou cópias.
# - Não removemos o elemento, portanto, a pilha permanece intacta.