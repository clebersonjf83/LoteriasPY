"""
Classe da Lotofacil
"""

from random import randrange


class Lotofacil:

    def __init__(self, *args, dezenas=15):
        """
        Cria um objeto do tipo Lotofacil.
        :param args: Se vazio, cria um jogo surpresinha com a quantidade de dezenas padrao (15)
        :param dezenas: Quantidade de dezenas da aposta (15-18)
        """
        self.__dezenas = dezenas
        if len(args) == 0:
            self.__jogo = self.__surpresinha()
        elif len(args) < 15 or len(args) > 18:
            raise ValueError('Os parametros de jogo devem ser inteiros entre 1 e 25')
        else:
            self.__jogo = set(args)

    def __repr__(self):
        l_exib = list(self.__jogo)
        l_exib.sort()
        return str(l_exib)

    def __iter__(self):
        yield set(self.__jogo)

    def __len__(self):
        return self.__dezenas

    def __surpresinha(self):
        """
        Retorna um conjunto(set) com numeros inteiros entre 1 e 25
        :return: set
        """
        retorno = set()
        while len(retorno) < self.__dezenas:
            # resultado.add(secrets.choice(range(1, 61)))
            retorno.add(randrange(1, 26, 1))
        return set(retorno)

    @property
    def jogo(self):
        return set(self.__jogo)


if __name__ == '__main__':
    print('Essa classe deve ser apenas instanciada internamente.')
