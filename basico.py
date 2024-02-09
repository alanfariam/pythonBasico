nome = input("Didite o nome: ")
print(type(nome))
print(nome)
nome = str(nome)
nome = str.upper(nome)
print(nome)
nome = str.strip(nome)
print(nome)
nome = nome.replace('A','@')
print(nome)

if 10 > 11 or 11 > 12:
    print('teste')
elif 10 == 10:
    print('condição ' + nome)
else:
    print('else')

contador = 1

print('W')
while contador <= 2:
    print(nome)
    contador = contador + 1
print('F')
for contador in range(1,5):
    print(nome)

#listas
lista = ['alan','julia','paula','guilherme']

print(len(lista))
print(lista[2:4])
print(lista[1:])

lista.append('Brokinha')
lista.extend(['Nina','Zico'])
lista.remove('Zico')

for i in lista:
    print(i)

#Dicionarios
dicionario = {'CPF':'0123',
              'NOME': 'Alan'}

print(dicionario)
print(dicionario['CPF'])
dicionario['CPF'] = '01239186690'
print(dicionario['CPF'])
dicionario['RG'] = 'MG105234324'
dicionario.pop('RG')
print(dicionario)
print('*********')
for dic in dicionario.values():
    print(dic)


#def media(lista)
#    calculo = sum(lista) / len(lista)
#    return calculo

#resultado = media(notas)
    





