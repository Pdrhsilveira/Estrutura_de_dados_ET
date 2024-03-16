#Considere listas encadeadas de valores inteiros e
#implemente uma função para retornar o número de nós da
#lista que possuem o campo info com valores maiores do
#que n. Esta função deve obedecer ao protótipo:

#def maiores(lst, n):

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

def maiores(lst, n):
    count = 0
    atual = lst
    while atual is not None:
        if atual.info is not None and atual.info > n:
            count += 1
        atual = atual.prox
    return count

lst = cria_lista()
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)

n = 20
print("Número de nós com valores maiores que",n,":", maiores(lst, n))  
