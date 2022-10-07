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


if __name__ == '__main__':
    aposta1 = Quina(1, 5, 6, 15, 22, 28, dezenas=6)   # (surpresinha automatica para faltantes)
    aposta2 = Quina(dezenas=5)
    aposta3 = Quina(dezenas=5)
    aposta4 = Quina(dezenas=5)
    concursos = 1                                        # Quantidade de concursos, comecando com o primeiro
    print(f'Suas apostas: \n{aposta1}, \n{aposta2}, \n{aposta3}')                     # Apresenta a aposta ao usuario
    print(f'Quantidade de dezenas: {len(aposta1)}')
    concurso_loteria = Sorteio.Sorteio(aposta1)          # Cria um objeto do tipo sorteio
    resultado_loteria = concurso_loteria.sortear()       # Executa o sorteio e armazena na variavel

    # Para chamar o método conferir da classe Sorteio, um objeto Sorteio deve ter sido instanciado previamente
    # Antes da conferencia, deve ser executado um sorteio pelo método sortear()
    # Deve ser informado o parametro ao metodo conferir() a propriedade jogo do ojbeto de aposta, Megasena, Quina...
    while concurso_loteria.conferir(aposta1.jogo) < concurso_loteria.sorteio_len:
        resultado_loteria = concurso_loteria.sortear()    # Novo sorteio
        concursos += 1                                      # Controla o numero de concursos
        print(f'\rConcursos {concursos:,}', end='')
    resultado_loteria = list(resultado_loteria)
    resultado_loteria.sort(key=lambda ele: (0, int(ele)) if isinstance(ele, int) else (1, ele))

    print('\n_______________________________________________________')
    print(f'Foram necessarios {concursos:,} concursos. ')
    print(f'Numeros sorteados: {resultado_loteria}')

