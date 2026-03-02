# =========================================
# Lista 1 – Algoritmos Básicos em Python
# =========================================

# ===== Questão 1 =====
print("Olá, Mundo!")

# ===== Questão 2 =====
num = 10
print("Antecessor:", num - 1)
print("Sucessor:", num + 1)

# ===== Questão 3 =====
a, b = 5, 3
print("Soma:", a + b)

# ===== Questão 4 =====
n1, n2, n3 = 7, 8, 9
print("Média:", (n1 + n2 + n3) / 3)

# ===== Questão 5 =====
metros = 2
print("Centímetros:", metros * 100)

# ===== Questão 6 =====
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# ===== Questão 7 =====
c = 25
print("Fahrenheit:", (c * 9/5) + 32)

# ===== Questão 8 =====
base, altura = 4, 6
print("Área do retângulo:", base * altura)

# ===== Questão 9 =====
num = 4
print("Par" if num % 2 == 0 else "Ímpar")

# ===== Questão 10 =====
num = -3
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Zero")

# ===== Questão 11 =====
peso, altura = 70, 1.75
imc = peso / (altura ** 2)
print("IMC:", imc)

# ===== Questão 12 =====
a, b, c = 10, 20, 15
print("Maior:", max(a, b, c))

# ===== Questão 13 =====
num = 9
print("Múltiplo de 3" if num % 3 == 0 else "Não múltiplo")

# ===== Questão 14 =====
num = 5
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print("Fatorial:", fatorial)

# ===== Questão 15 =====
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b

# ===== Questão 16 =====
for i in range(1, 101):
    print(i)

# ===== Questão 17 =====
n = 10
print("Soma até N:", sum(range(1, n + 1)))

# ===== Questão 18 =====
soma = 0
numeros = [5, 3, 2, 0]
for num in numeros:
    if num == 0:
        break
    soma += num
print("Soma total:", soma)

# ===== Questão 19 =====
contador = 0
for i in range(1, 51):
    if i % 2 == 0:
        contador += 1
print("Quantidade de pares:", contador)

# ===== Questão 20 =====
num = "123"
print("Invertido:", num[::-1])

# ===== Questão 21 =====
palavra = "arara"
print("É palíndromo" if palavra == palavra[::-1] else "Não é")

# ===== Questão 22 =====
texto = "algoritmo"
vogais = "aeiou"
contador = sum(1 for letra in texto if letra in vogais)
print("Vogais:", contador)

# ===== Questão 23 =====
frase = "ola mundo python"
print(frase.replace(" ", "-"))

# ===== Questão 24 =====
lista = [4, 7, 1, 9, 2]
print("Maior:", max(lista))
print("Menor:", min(lista))

# ===== Questão 25 =====
lista.sort()
print("Ordenada:", lista)

# ===== Questão 26 =====
lista = [1, 2, 2, 3, 4, 4]
print("Sem duplicados:", list(set(lista)))

# ===== Questão 27 =====
lista = [1, 2, 3, 4]
print("Soma:", sum(lista))

# ===== Questão 28 =====
lista = [1, 2, 2, 3]
print("O número 2 aparece:", lista.count(2), "vezes")

# ===== Questão 29 =====
pessoa = {"nome": "Raphael", "idade": 20}
print(pessoa)

# ===== Questão 30 =====
pessoa["idade"] = 21
print(pessoa)

# ===== Questão 31 =====
def soma(a, b):
    return a + b
print("Soma função:", soma(5, 3))

# ===== Questão 32 =====
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print("7 é primo?", eh_primo(7))

# ===== Questão 33 =====
import math
def area_circulo(raio):
    return math.pi * raio ** 2
print("Área círculo:", area_circulo(5))

# ===== Questão 34 =====
def fatorial_rec(n):
    if n <= 1:
        return 1
    return n * fatorial_rec(n - 1)
print("Fatorial recursivo:", fatorial_rec(5))

# ===== Questão 35 =====
quadrados = [i**2 for i in range(1, 11)]
print(quadrados)

# ===== Questão 36 =====
pares = [i for i in range(1, 21) if i % 2 == 0]
print(pares)

# ===== Questão 37 =====
with open("arquivo.txt", "w") as f:
    f.write("Linha 1\nLinha 2\nLinha 3\n")

with open("arquivo.txt", "r") as f:
    print("Número de linhas:", len(f.readlines()))

# ===== Questão 38 =====
with open("arquivo2.txt", "w") as f:
    f.write("Escrevendo no arquivo.")

# ===== Questão 39 =====
opcao = 1
while opcao != 2:
    print("1 - Olá")
    print("2 - Sair")
    opcao = 2
    print("Olá!")

# ===== Questão 40 =====
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Erro: divisão por zero!")
