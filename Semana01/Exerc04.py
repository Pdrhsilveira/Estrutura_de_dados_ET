#Implemente uma função que receba duas listas
#encadeadas de valores inteiros e retorne a lista resultante
#da concatenação das duas listas recebidas como
#parâmetros, isto é, após a concatenação, o último
#elemento da primeira lista deve apontar para o primeiro
#elemento da segunda lista.
#○ Esta função deve obedecer ao protótipo:

#def concatena(l1, l2):

class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo = Lista(valor)
    if lst is None:
        return novo
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    atual.prox = novo
    return lst

def concatena(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    atual = l1
    while atual.prox is not None:
        atual = atual.prox
    
    atual.prox = l2
    
    return l1

l1 = cria_lista()
l1 = insere_lista(l1, 10)
l1 = insere_lista(l1, 20)
l1 = insere_lista(l1, 30)

l2 = cria_lista()
l2 = insere_lista(l2, 40)
l2 = insere_lista(l2, 50)
l2 = insere_lista(l2, 60)

lista_concatenada = concatena(l1, l2)

print("Lista concatenada:")
atual = lista_concatenada
while atual is not None:
    print(atual.info)
    atual = atual.prox

