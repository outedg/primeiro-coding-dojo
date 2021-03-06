import pytest
'''
DESAFIO
O objetivo é fazer um juiz de Jokenpo
que dada a jogada dos dois jogadores
informa o resultado da partida

REGRAS
 Não importa o nível de conhecimento
 Objetivo principal é aprender algo, ou compartilhar algo que sabe
 Concluir o desafio não é o Objetivo
 Baby Step (o mais simples/básico)
 Trabalhar orientado a Teste (TDD) [Red/Green/Refactoring]
 Piloto e co-piloto (piloto coda, co-piloto dá os palpites)
 Enquanto os teste não estiverem passando, somente o par pode falar
 Expectador podem falar, somente quando o teste estiverem passando
    ou quando pedirem ajuda;
DESAFIO 
JOKENPO


ANDREY
LEANDRO
EDGAR
LUCAS
PATRIK
VINICIUS
'''

#ATRIBUIÇÕES
PEDRA: str = "pedra"
EMPATE: str = "empate"
TESOURA: str = "tesoura"
PAPEL: str = "papel"
 
def jokenpo(player: str, player2: str) -> str:
    if(player == TESOURA and player2 == PAPEL):
        return player2
    return PAPEL

# def test_inicial_empate() -> None:
#     assert jokenpo(PEDRA, PEDRA) == EMPATE


def test_tesoura_ganha_de_papel() -> None:
    assert jokenpo(TESOURA, PAPEL) == TESOURA

def test_papel_ganha_de_pedra() -> None:
    assert jokenpo(PAPEL, PEDRA) == PAPEL