#!/usr/bin/python
# Programa que conjuga verbos regulares
# versão 0.05 por Cesar Brod em 21/08/2013
# Atualizada para o Python 3 em 31/10/2023

# Primeiro, criamos listas com as terminações de verbos regulares
pessoas = ['Eu', 'Tu', 'Ele', 'Nós', 'Vós', 'Eles']
conjuga_ar = ['o', 'as', 'a', 'amos', 'ais', 'am']
conjuga_er = ['o', 'es', 'e', 'emos', 'eis', 'em']
conjuga_ir = ['o', 'es', 'e', 'imos', 'is', 'em']

# a seguir, pedimos que o usuário informe o verbo
verbo = input("Digite o infinitivo de um verbo regular:")

termina_em = verbo[-2:]  # separa a terminação do verbo

# agora, de acordo com a terminação do verbo, conjuga apropriadamente
if termina_em == 'ar':
    for i in range(6):  # repete seis vezes, percorrendo a lista
        print(pessoas[i]+' '+verbo[:-2]+conjuga_ar[i])
elif termina_em == 'er':
    for i in range(6):  # repete seis vezes, percorrendo a lista
        print(pessoas[i]+' '+verbo[:-2]+conjuga_er[i])
elif termina_em == 'ir':
    for i in range(6):  # repete seis vezes, percorrendo a lista
        print(pessoas[i]+' '+verbo[:-2]+conjuga_ir[i])
else:
    print('Tem certeza que '+verbo+' é um verbo regular?')
