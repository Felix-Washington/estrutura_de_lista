from lista import Lista
import os


class Main:
    def __init__(self):
        self.__lista = Lista(4)
        self.__executando = True

    def inicia(self):
        posicao = 0
        dado = 0
        while self.__executando:
            #os.system('cls' if os.name == 'nt' else 'clear')
            print("\n")
            print("1 - Inserir elemento na frente")
            print("2 - Inserir elemento no final")
            print("3 - Inserir elemento na posição desejada")
            print("4 - Buscar elemento específico via dado")
            print("5 - Mostra todos os elementos")
            print("6 - Remover elemento no final")
            print("7 - Remover elemento no início")
            print("8 - Inserir antes do Atual")

            opcao = int(input("Digite uma opção\n"))
            if opcao < 5 or opcao > 7:
                dado = int(input("Digite um valor\n"))
                if opcao == 3:
                    posicao = int(input("Digite a posição desejada"))

            if opcao == 1:
                self.__lista.inserirNaFrente(dado)
            elif opcao == 2:
                self.__lista.inserirNoFinal(dado)

            elif opcao == 3:
                self.__lista.inserir_na_posicaok(posicao, dado)

            elif opcao == 4:
                print(self.__lista.buscar(dado))

            elif opcao == 5:
                self.__lista.mostrar_elementos()

            elif opcao == 6:
                self.__lista.remover_elemento_fim()

            elif opcao == 7:
                self.__lista.remover_elemento_inicio()

            elif opcao == 8:
                self.__lista.inserirAntesDoAtual(dado)

            elif opcao == 9:
                self.__lista.inserirDepoisDoAtual()

            elif opcao == 10:
                self.__lista.avancarKPosicoes()

            elif opcao == 0:
                self.__executando = False

            else:
                print("Digite uma opção válida")
