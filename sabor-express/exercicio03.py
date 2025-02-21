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

for num in range(10, 0, -1):
    print(num)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
