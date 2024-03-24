class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return None

def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo

def remover_lista(lst, valor):
    atual = lst
    ant = None
    while atual is not None:
        if atual.info == valor:
            if ant is not None:
                ant.prox = atual.prox
            else:
                lst = atual.prox
            atual = atual.prox

        else:
            ant = atual
            atual = atual.prox
    return lst

lst = None
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)
lst = insere_lista(lst, 30)

print("Lista original:")
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox

v = 30
lst = remover_lista(lst, v)

print("Lista após remover o elemento anterior a", v)
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox
