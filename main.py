"""
Modulo principal
"""

from Megasena import Megasena
from Duplasena import Duplasena
from Quina import Quina
from Lotofacil import Lotofacil
from Lotomania import Lotomania
from Diadesorte import Diadesorte
import Sorteio
import sys
# import tela_principal


if __name__ == '__main__':
    parametros = sys.argv
    aposta1 = Megasena(1, 12, 23, 44, 56, 33)   # (surpresinha automatica para faltantes)
    concursos = 1                                        # Quantidade de concursos, comecando com o primeiro
    print(f'Sua aposta: {aposta1}')                     # Apresenta a aposta ao usuario
    print(f'Quantidade de dezenas: {len(aposta1)}')
    concurso_loteria = Sorteio.Sorteio(aposta1)          # Cria um objeto do tipo sorteio
    resultado_loteria = concurso_loteria.resultado       # Executa o sorteio e armazena na variavel
    grafico = [0, 0, 0]

    while concurso_loteria.conferir(aposta1.jogo) < concurso_loteria.sorteio_len:
        resultado_loteria = concurso_loteria.resultado()    # Novo sorteio
        concursos += 1                                      # Controla o numero de concursos
        print(f'\rConcursos {concursos:,}', end='')
        if concurso_loteria.conferir(aposta1.jogo) == 4:
            grafico[0] += 1
        elif concurso_loteria.conferir(aposta1.jogo) == 5:
            grafico[1] += 1

    grafico[2] += 1
    print('\n_______________________________________________________')
    print(f'Foram necessarios {concursos:,} concursos. ')
    print(f'Numeros sorteados: {resultado_loteria}')
    print(f'Dados relevantes: {grafico}')
