from elemento import Elemento


class Lista:

    def __init__(self, n_elementos):
        self.__n_elementos = n_elementos
        self.__atual = None
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0

    def inserirNaFrente(self, dado):
        novo = Elemento(dado)
        if self.lista_vazia():
            self.__inicio = novo
            self.__fim = novo

        else:
            self.__atual = self.__inicio
            self.__inicio = novo
            self.__inicio.posterior = self.__atual

        self.__tamanho += 1

    def inserirNoFinal(self, dado):
        novo_elemento = Elemento(dado)
        if self.lista_vazia():
            self.__inicio = novo_elemento

        else:
            self.__fim.posterior = novo_elemento
            novo_elemento.anterior = self.__fim
            novo_elemento.posterior = None

        self.__fim = novo_elemento
        self.__atual = novo_elemento
        self.__tamanho += 1

    def inserir_na_posicaok(self, k, dado):
        contador = 0
        self.__atual = self.__inicio

        if k > self.__tamanho + 1:
            print("Nao existe essa posicao")
        elif k == self.__tamanho:
            self.inserirNoFinal(dado)
        elif k == 0:
            self.inserirNaFrente(dado)
        else:
            novo_elemento = Elemento(dado)
            while contador <= self.__tamanho:
                print(self.__atual.dado)
                if self.__atual is not None and k == contador:
                    aux = self.__atual.posterior
                    aus = self.__atual.anterior
                    self.__atual.posterior = novo_elemento
                    novo_elemento.posterior = aux.posterior
                    aux.anterior = novo_elemento
                    novo_elemento.anterior = self.__atual


                    print("dado", self.__atual.dado)
                    print("ant",self.__atual.anterior.dado)
                    print("pos", self.__atual.posterior.dado)
                    break

                else:
                    self.__atual = self.__atual.posterior

                contador += 1
            #elemento = avancarKPosicoes(k)
            #nesse else tem que percorrer as posicoes ate chegar na posicao desejada e inserir o novo elemento
            #se a posicao desejada estiver vazia

    def buscar(self, buscado):
        self.__atual = self.__inicio
        contador = 0
        while contador < self.__tamanho:

            if self.__atual.dado == buscado:
                return "Elemento: ", self.__atual.dado
            self.__atual = self.__atual.posterior
            contador += 1
        return "O elemento não está na lista."

    def mostrar_elementos(self):
        contador = 0
        index = 0
        self.__atual = self.__inicio

        if self.__inicio is None:
            print("Não há elementos")
        while contador < self.__tamanho:
            if self.__atual is not None:
                print("Index = ", index, " dado = ", self.__atual.dado)
                index += 1

            self.__atual = self.__atual.posterior

            contador += 1

    def remover_elemento_fim(self):
        if self.__tamanho == 1:
            self.__inicio = None
            self.__tamanho -= 1

        if self.__inicio is not None:
            self.__fim = self.__fim.anterior
            self.__fim.posterior = None
            self.__tamanho -= 1
        else:
            print("Não há elementos")

    def remover_elemento_inicio(self):
        if self.__tamanho == 1:
            self.__inicio = None
            self.__tamanho -= 1

        elif self.__tamanho == 0:
            print("Não há elementos")

        else:
            self.__inicio = self.inicio.posterior
            self.__tamanho -= 1

    def inserirAntesDoAtual(self, dado):

        #self.__atual = self.__inicio.posterior

        #print(self.__atual.anterior.dado)
        #print(self.__atual.dado)
        #elemento_atual = self.buscar(dado)
        novo = Elemento(dado)
        if self.__atual == self.__inicio:
            print("tst")
            self.inserirNaFrente(dado)

        else:
            aux = self.__atual.anterior
            self.__atual.anterior = novo
            novo.anterior = aux
            novo.anterior.posterior = novo
            novo.posterior = self.__atual

            #novo.anterior = self.__atual.anterior
            #novo.posterior = self.__atual
            #elemento_atual.anterior = novo.dado

        #self.__atual = novo.dado

    def inserirDepoisDoAtual(self, dado):
        if self.__atual == self.__fim:
            self.inserirNoFinal(dado)

        else:

            elemento_atual = self.__atual
            novo = Elemento(dado)
            novo.anterior = elemento_atual
            novo.posterior = elemento_atual.posterior
            elemento_atual.posterior = novo.dado
            self.__atual = novo.dado

    def avancarKPosicoes(self, k):
        elemento = self.__inicio
        contador = 0

        while contador <= self.__tamanho:
            if contador == k:
                elemento = elemento.dado
                self.__atual = elemento
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
            self.__atual = elemento
            return elemento
        raise ValueError("Nao existe essa posicao")


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