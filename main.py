from lista import Lista
import os


class Main:
    def __init__(self):
        self.__lista = Lista(4)
        self.__executando = True

    def inicia(self):
        while self.__executando:
            #os.system('cls' if os.name == 'nt' else 'clear')
            print("1 - Inserir elemento na frente")
            print("2 - Inserir elemento no final")
            print("3 - Inserir elemento na posição desejada")
            print("4 - Buscar elemento")
            print("5 - Inserir elemento na frente")
            print("6 - Inserir elemento na frente")

            opcao = int(input("Digite uma opção\n"))
            dado = int(input("Digite um valor\n"))

            if opcao == 1:
                self.__lista.inserirNaFrente(dado)
            elif opcao == 2:
                self.__lista.inserirNoFinal(dado)

            elif opcao == 4:
                self.__lista.buscar(dado)

            elif opcao == 0:
                self.__executando = False


            print("lista_inicio" ,self.__lista.inicio.dado)
            print("lista_fim", self.__lista.fim.dado)
            #print(self.__lista.atual.dado)
