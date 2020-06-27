# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:07:42 2020

@author: Lucas Oliveira
"""
#Variáveis globais
feminino=[] #Lista dos nomes femininos
masculino=[] #Lista do nomes masculinos
idadeMasculina=[] #Lista de idades
idadeFeminina=[] #Lista de idades
pessoas=int(0) #Contador de pessoas
pessoasCadastradas=() #Tupla de resultados
pessoasDiferentes=set() #Conjunto de Pessoas exclusivas
idadesDiferentes=set() #Conjunto de idades distintas
soma=int(0) #Recebe a soma das idades
nomesFemininos={} #Dicionario de idades: nomes
nomesMasculinos={} #Dicionario de idades: nomes
x = int(1) #variável de saída do 1ºwhile

#Entrada de dados
print('\n\n##### Cadastro de Pessoas #####')
while x == 1:
    nome=input('Digite o nome: ')
    while nome == '': #Validação campo vazio
        nome=input('Digite um nome: ')
    idade=int(input('Digite a idade: '))
    while type(idade) != int: #validação de campo int
        idade={int(input('Digite um número inteiro válido: '))}
    soma=soma+idade #Somando as idades
    idadesDiferentes.add(idade) #Separando os nomes exclusivos
    sexo=int(input('Digite 1 para masculino ou 2 para Feminino: '))
    
    #Categorização de pessoas por sexo
    while sexo > 2:
        sexo=int(input('Digite um valor válido (1 ou 2): '))
    if sexo==2:
        feminino.append(nome) #Carregando lista de pessoas
        idadeFeminina.append(idade)#Carregamento lista para dicionário
    else:
        masculino.append(nome)#Carregando lista de pessoas
        idadeMasculina.append(idade)#Carregamento lista para dicionário
    x=int(input('Deseja realizar um novo cadastro? 1-Sim ou 0-não: '))
    pessoas=pessoas+1
    
    
#Processar dados
media=((float(soma)/float(pessoas))) #calcula a média das idades
pessoasCadastradas=(pessoas,format(media,'.2f')) 
pessoasDiferentes.update(masculino) #Carregando conjunto para diferenciar pessoas
pessoasDiferentes.update(feminino) #Carregando conjunto para diferenciar pessoas

#Tentei usar Dicionários por dias e não consegui iterar eles
'''list(zip(idadeMasculina,masculino))
nomesMasculinos=dict(zip(idadeMasculina,masculino))
list(zip(idadeFeminina,feminino))
nomesFemininos=dict(zip(idadeFeminina,feminino))'''

#Saída de dados
print('\n\n\n      __Dados coletados__')    
print('Cadastro de pessoas exclusivas: ',len(pessoasDiferentes))
print('Idades diferentes cadastradas: ', len(idadesDiferentes))
print('Pessoas Cadastradas / Médias das idades: ',pessoasCadastradas)
print('\nHomens cadastrados: ',len(masculino))
for x in masculino:
    print(x)
print('\nMulheres cadastradas',len(feminino))
for x in feminino:
    print(x)
    

