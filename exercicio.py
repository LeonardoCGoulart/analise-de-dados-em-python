# -*- coding: utf-8 -*-
print("EXERCICIO 01:")


#Três alunos, X, Y e Z, estão matriculados em um curso de inglês.
# Para avaliar esses alunos, o professor optou por fazer cinco provas.
# Para que seja aprovado nesse curso, o aluno deverá ter a média aritmética
# das notas das cinco provas maior ou igual a 6. Na tabela, estão dispostas
# as notas que cada aluno tirou em cada prova. (ENEM 2017)

# Aluno  NOTA1  NOTA 2  NOTA3    NOTA4   NOTA5
# X         5   5       5          10       6
# Y         4   9       3           9       5
# Z         5   5       8           5       6

##################################################
# Com base nos dados da tabela e nas informações dadas, ficará(ão) reprovado(s)

# a) apenas o aluno Y.
# b) apenas o aluno Z.
# c) apenas os alunos X e Y.
# d) apenas os alunos X e Z.
# e) os alunos X, Y e Z.

#importa a biblioteca numpy para usar a função de calcular média
import numpy as np

#transforma as notas em uma lista
notasAlunoX = [5, 5, 5, 10, 6]
notasAlunoY = [4, 9, 3, 9, 5]
notasAlunoZ = [5, 5, 8, 5, 6]

#calcula a media de cada aluno
mediaAlunoX = np.mean(notasAlunoX)
mediaAlunoY = np.mean(notasAlunoY)
mediaAlunoZ = np.mean(notasAlunoZ)

#função para ver se esta aprovado
def estaAprovado(nota):
    if(nota >= 6):
        return "aprovado"
    else:
        return "reprovado"

#resultado da questão
print("o aluno X esta ", estaAprovado(mediaAlunoX))
print("o aluno Y esta ", estaAprovado(mediaAlunoY))
print("o aluno Z esta ", estaAprovado(mediaAlunoZ))

#dessa forma o Aluno Z é o unico reprovado, logo alternativa B

###########################################################################################
#exercio 2 (ENEM 2015)
print("EXERCICIO 02:")

#Em uma seletiva para a final dos 100 metros livres de natação, numa olimpíada,
#os atletas, em suas respectivas raias, obtiveram os seguintes tempos:

# raia          tempo
# 1             20.90
# 2             20.90
# 3             20.50
# 4             20.80
# 5             20.60
# 6             20.60
# 7             20.90
# 8             20.96

#A mediana dos tempos apresentados no quadro é?

#adicionando os tempos numa lista
tempo = [20.90, 20.90, 20.50, 20.80, 20.60, 20.60, 20.90, 20.96]

#conferindo se a quantidade esta ok
print("tamanho da lista tempo:")
print(len(tempo))

#resultado
print("resultado:", np.median(tempo))

#logo a resposta é: 20.85


