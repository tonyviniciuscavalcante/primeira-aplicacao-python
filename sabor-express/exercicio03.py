# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista_numerica = []
i = 1

while i <= 10:
    lista_numerica.append(i)
    i +=1

print(lista_numerica)

lista_nomes = ['Tony', 'Heloisa', 'Helena', 'Bento']
print(lista_nomes)

lista_anos = [1999, 2015]

print(f'Nasci no ano: {lista_anos[0]} e estamos no ano: {lista_anos[1]}')

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

lista_filmes = ['Homem-aranha', 'Super-man', 'Homem de ferro']

for filme in lista_filmes:
    print(f'- {filme}')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0

for num in range(1, 11):
    if num % 2 != 0:
        soma += num

print("Soma dos números ímpares de 1 a 10:", soma)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# lista_numerica = []
# lista_decrescente = []
# i = 1
#
# while i <= 10:
#     lista_numerica.append(i)
#     i +=1
#
# print(lista_numerica)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.



# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.



# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


