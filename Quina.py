"""
Classe da Quina
"""

import secrets

MAXBET = 15
MINBET = 5
MINNUM = 1
MAXNUM = 80
RANGEBET = range(MINNUM, MAXNUM + 1)


class Quina:

    def __init__(self, *args, dezenas=5):
        """
        Cria um objeto do tipo Quina.
        :param args: Se vazio, cria um jogo surpresinha com a quantidade de dezenas(padrao=5)
        :param dezenas: Quantidade de dezenas da aposta (5-15)
        """
        assert len(args) <= MAXBET, f'Esperado no máximo {MAXBET} dezenas. (Passadas {len(args)})'
        assert MINBET <= dezenas <= MAXBET and isinstance(dezenas, int), \
            f'Parametro dezenas deve ser inteiro entre {MINBET} e {MAXBET}. (Passadas {dezenas})'
        assert self.__checkargs(args), f'Lotofácil usa números inteiros entre 0{MINNUM} e {MAXNUM}'
        self.__dezenas = dezenas
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
        count = len(RANGEBET)
        retorno = set(fixos)
        numeros = [x for x in range(1, count + 1)]
        while len(retorno) < self.__dezenas:
            retorno.add(numeros.pop(secrets.choice(range(0, count))))
            count -= 1
        return set(retorno)

    @property
    def jogo(self):
        return set(self.__jogo)

    @staticmethod
    def __checkargs(numeros):
        if len(numeros) == 0:
            return True
        else:
            for i in numeros:
                if i not in RANGEBET:
                    return False
            return True


if __name__ == '__main__':
    print('Essa classe deve ser apenas instanciada internamente.')
