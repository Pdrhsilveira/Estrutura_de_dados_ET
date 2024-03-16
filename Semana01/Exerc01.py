#Implemente uma função que tenha como valor de
#retorno o comprimento de uma lista encadeada, isto é
#calcule o número de nós de uma lista. Esta função
#deve obedecer ao protótipo:

#def list_comprimento(lst):

class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo

def lista_comprimento(lst):
    tamanho = 0
    atual = lst
    while atual is not None:
        tamanho += 1
        atual = atual.prox
    tamanho -=1 # gambiarra
    return tamanho

lst = cria_lista()
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)
lst = insere_lista(lst, 50)

print("Comprimento da lista:", lista_comprimento(lst)) 
