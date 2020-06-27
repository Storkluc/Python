print('### FOLHA MÊS DE MARÇO')
print()

"""Setor das variaveis do fechamento da folha"""
diastrab = int(input('Dias trabalhados: ')) #Dias Trabalhados
horastrab = float(input('Horas de trabalho diário: ')) #Quantas horas por dia
valorhoratrab = float(input('Valor da hora trabalhada: '))#Valor por hora trabalhada
horaextra = float(input('Horas extras: ')) #Horas extras de trabalho
valorhoraextra = float(input('Valor da hora extra trabalhada: '))
vcombustivel = float(input('Valor vale combustível: ')) #Valor do Vale Combustível
valimentacao = float(input('Valor vale alimentação: ')) #Valor do Vale Alimentação
descontfalta = float(input('Desconto falta/atraso: ')) #Descontos de faltas/atrasos
planodesaude = float(input('Desconto plano de saude: ')) #Desconto do plano de saude
planoodonto = float(input('Desconto plano odontológico: ')) #Desconto plano Odontológico
numerodependentes = int(input('Número de dependentes: '))
descontodep = float(input('Desconto dependente: ')) #Descontos de estudos do dependentes
salariobruto = float(0)
descontos = float(0)

print()
print('----Resumo do fechamentos da folha de março----')
print()

"Setor de cálculos da folha"
salariobruto = diastrab*horastrab
horaextra = horaextra*valorhoraextra
salariobruto = salariobruto


"Setor de resultados dos cálculos da folha"
print(' (+) SALÁRIO BRUTO.........R$')
print(' (-) Descontos por falta...R$')
print(' (-) Plano de saúde........R$')
print(' (-) Plano Odontológico....R$')
print(' (-) Auxílio escolar.......R$')
print(' (=) BRUTO COM DESCONTOS...R$')
print(' (-) IR (11%)..............R$')
print(' (-) INSS (8%).............R$')
print(' (-) Sindicato (5%)........R$')
print(' (=) SALÁRIO LIQUIDO.......R$')
print()
print('______________________________________________________________________')
