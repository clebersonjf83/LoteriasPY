"""
Classe da +Milionária
"""

import secrets

MAX_BET = 12
MIN_BET = 6
MIN_NUM = 1
MAX_NUM = 50
MIN_TREVOS = 2
MAX_TREVOS = 6
RANGE_TREVO = range(1, 7)
RANGEBET = range(MIN_NUM, MAX_NUM + 1)


class Milionaria:

    def __init__(self, *args, dezenas=MIN_BET, num_trevos=2, trevos: tuple):
        """
        Cria um objeto do tipo +Milionaria.
        :param args: Se vazio, cria um jogo surpresinha com a quantidade de dezenas(padrao=6)
        :param dezenas: Quantidade de dezenas da aposta (6-15)
        """
        assert len(args) <= MAX_BET, f'Esperado no máximo {MAX_BET} dezenas. (Passadas {len(args)})'
        assert MIN_BET <= dezenas <= MAX_BET and isinstance(dezenas, int), \
            f'Parametro dezenas deve ser inteiro entre {MIN_BET} e {MAX_BET}. (Foi informado {dezenas})'
        assert self.__checkargs(args), f'+Milionária usa números inteiros entre 0{MIN_NUM} e {MAX_NUM}'
        assert MIN_TREVOS <= num_trevos <= MAX_TREVOS, f'Devem ser escolhidos de 2 a 6 trevos.'
        self.__dezenas = dezenas
        self.__num_trevos = num_trevos
        self.__trevos = set(trevos)
        self.__jogo = self.__surpresinha(set(trevos), set(args))

    def __repr__(self):
        l_exib = list(self.__jogo)
        l_exib.sort()
        return str(l_exib)

    def __iter__(self):
        yield set(self.__jogo)

    def __len__(self):
        return self.__dezenas + len(self.__trevos)

    @staticmethod
    def __checkargs(numeros):
        if len(numeros) == 0:
            return True
        else:
            for i in numeros:
                if i not in RANGEBET:
                    return False
            return True

    def __surpresinha(self, trevos=(), fixos=()):
        """
        Retorna um conjunto(set) com numeros inteiros entre 1 e 50
        :return: set
        """
        count = len(RANGEBET)
        retorno = set(fixos)
        numeros = [x for x in range(1, count + 1)]
        while len(retorno) < self.__dezenas:
            retorno.add(numeros.pop(secrets.choice(range(0, count))))
            count -= 1

        # Escolhe os trevos
        count_t = len(RANGE_TREVO)
        retorno_t = set(trevos)
        numeros_t = [x for x in range(1, count_t + 1)]
        while len(retorno_t) < self.__num_trevos:
            retorno_t.add(numeros_t.pop(secrets.choice(range(0, count_t))))
            count_t -= 1
        retorno.add(tuple(retorno_t))
        return set(retorno)

    def sorteio(self):
        return self.__surpresinha()

    @property
    def jogo(self):
        return set(self.__jogo)


if __name__ == '__main__':
    print('Essa classe deve ser apenas instanciada internamente.')
