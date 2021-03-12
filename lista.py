from elemento import Elemento


class Lista:

    def __init__(self, n_elementos):
        self.__nElementos = n_elementos
        self.__atual = None
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0

    def inserirNaFrente(self, dado):
        novo = Elemento(dado, self.__tamanho)
        if self.lista_vazia():
            self.__inicio = novo
            self.__fim = novo
            self.__tamanho += 1
        else:
            novo.anterior = self.__inicio
            self.__inicio = novo
            #anterior = novo.anterior(None)
            #posterior = novo.posterior(self.__inicio)
            self.__tamanho += 1

        self.__atual = novo

    def inserirNoFinal(self, novo_elemento):
        novo = Elemento(novo_elemento, self.__tamanho)
        if self.lista_vazia():
            self.__inicio = novo
            self.__fim = novo
            self.__tamanho += 1
            self.__atual = self.__inicio

        else:
            self.__fim.posterior = novo
            novo.anterior = self.__fim
            novo.posterior = None
            self.__fim = novo
            self.__tamanho += 1

            if self.__atual.posterior.posterior is not None:
                print("ant ant", self.__atual.posterior.anterior.dado)



    def inserirAntesDoAtual(self, atual, novo_elemento):
        elemento_atual = self.buscar(atual)
        novo = Elemento(novo_elemento)
        novo.anterior = elemento_atual.anterior
        novo.posterior = elemento_atual
        elemento_atual.anterior = novo

    def inserirDepoisDoAtual(self, atual, novo_elemento):
        elemento_atual = self.buscar(atual)
        novo = Elemento(novo_elemento)
        novo.anterior = elemento_atual
        novo.posterior = elemento_atual.posterior
        elemento_atual.posterior = novo

    def inserirNaPosicaoK(self, k, novo_elemento):
        if k > self.__tamanho:
            raiseIndexError("Nao existe essa posicao")
        elif k == self.__tamanho:
            self.inserirNoFinal(novo_elemento)
        elif k == 0:
            self.inserirNaFrente(novo_elemento)
        else:
            elemento = avancarKPosicoes(k)
            #nesse else tem que percorrer as posicoes ate chegar na posicao desejada e inserir o novo elemento
            #se a posicao desejada estiver vazia

    def buscar(self, buscado):
        elemento = self.__inicio
        contador = 0
        while elemento:

            if elemento.dado == buscado:
                print("buscado",buscado)
                return elemento
            elemento = elemento.posterior
            contador +=1
        print("O elemento não está na lista")
        #raise ValueError("O elemento nao esta na lista")

    def avancarKPosicoes(self, k):
        elemento = self.__inicio
        contador = 0

        while contador <= self.__tamanho:
            if contador == k:
                elemento = elemento.dado
                return elemento
            else:
                elemento = elemento.proximo
                contador += 1

        raise IndexError("Nao existe essa posicao")

    def retrocederKPosicoes(self, k):
        elemento = self.__fim
        contador = self.__tamanho
        if k <= contador:
            elemento = elemento.anterior
            contador -= 1
        else:
            return elemento
        raise ValueError("Nao existe essa posicao")


    def mostrar_elementos(self):
        contador = 0

        while contador < self.__nElementos:
            if self.__atual.id == contador:
                print(self.__atual.dado)

                self.__atual.anterior = self.__atual.anterior.anterior
                contador += 1

    @property
    def atual(self):
        return self.__atual

    @atual.setter
    def atual(self, atual):
        self.__atual = atual

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    def lista_vazia(self):
        if self.__inicio is None:
            return True
        return False

    def lista_cheia(self):
        if self.__fim is not None:
            return True
        return False