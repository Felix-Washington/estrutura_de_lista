

class Elemento:
    def __init__(self, dado):
        self.__anterior = None
        self.__posterior = None
        self.__dado = dado

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, dado):
        self.__dado = dado

    @property
    def posterior(self):
        return self.__posterior

    @posterior.setter
    def posterior(self, posterior):
        self.__posterior = posterior
