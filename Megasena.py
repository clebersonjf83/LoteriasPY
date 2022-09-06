"""
Classe da Mega-Sena
"""

import secrets


class Megasena:

    def __init__(self, *args, dezenas=6):
        """
        Cria um objeto do tipo Megasena.
        :param args: Se vazio, cria um jogo surpresinha com a quantidade de dezenas(padrao=6)
        :param dezenas: Quantidade de dezenas da aposta (6-15)
        """
        self.__dezenas = dezenas
        if len(args) == 0:
            self.__jogo = self.__surpresinha()
        elif len(args) > 15:
            raise AttributeError('Aposta máxima 15 dezenas.')
        else:
            self.__jogo = self.__surpresinha(set(args))

    def __repr__(self):
        l_exib = list(self.__jogo)
        l_exib.sort()
        return str(l_exib)

    def __iter__(self):
        yield set(self.__jogo)

    def __len__(self):
        return self.__dezenas

    def __surpresinha(self, fixos=()):
        """
        Retorna um conjunto(set) com numeros inteiros entre 1 e 60
        :return: set
        """
        retorno = set(fixos)
        while len(retorno) < self.__dezenas:
            retorno.add(secrets.choice(range(1, 61, 1)))
        return set(retorno)

    @property
    def jogo(self):
        return set(self.__jogo)


if __name__ == '__main__':
    print('Essa classe deve ser apenas instanciada internamente.')
