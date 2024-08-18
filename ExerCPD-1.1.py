class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, valor):
        if not self.inicio:
            self.inicio = Nodo(valor)
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = Nodo(valor)

    def para_lista(self):
        resultado = []
        atual = self.inicio
        while atual:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado

    def ordenar_insercao(self):
        lista_ordenada = None
        atual = self.inicio
        while atual:
            proximo_nodo = atual.proximo
            lista_ordenada = inserir_ordenado(lista_ordenada, atual)
            atual = proximo_nodo
        self.inicio = lista_ordenada

def inserir_ordenado(inicio, novo_nodo):
    if not inicio or novo_nodo.valor < inicio.valor:
        novo_nodo.proximo = inicio
        inicio = novo_nodo
    else:
        atual = inicio
        while atual.proximo and atual.proximo.valor < novo_nodo.valor:
            atual = atual.proximo
        novo_nodo.proximo = atual.proximo
        atual.proximo = novo_nodo
    return inicio

# Testes
def testar_lista_encadeada(valores):
    lista_encadeada = ListaEncadeada()
    for valor in valores:
        lista_encadeada.adicionar(valor)
    lista_encadeada.ordenar_insercao()
    return lista_encadeada.para_lista()

#ordenados
valores_ordenados = [5, 15, 25, 35, 45]
print("Valores já ordenados:", testar_lista_encadeada(valores_ordenados))

#inversa
valores_invertidos = [55, 45, 35, 25, 15]
print("Valores na ordem inversa:", testar_lista_encadeada(valores_invertidos))

#duplicados
valores_duplicados = [18, 28, 18, 38, 28]
print("Valores duplicados:", testar_lista_encadeada(valores_duplicados))

#aleatórios
valores_aleatorios = [21, 4, 16, 99, 8]
print("Valores aleatórios:", testar_lista_encadeada(valores_aleatorios))
