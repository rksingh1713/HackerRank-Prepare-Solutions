import itertools

K, N = map(int, input().split())

lists = []
for i in range(N):
    lists.append(list(map(int, input().split()))[1:])

# Generar todas las posibles combinaciones de elementos de las listas
combinations = list(itertools.product(*lists))


# Función para calcular la suma de los cuadrados de una lista de números
def sum_of_squares(lst):
    return sum([x**2 for x in lst])


# Determinar la máxima suma posible
max_sum = 0
for c in combinations:
    sum_squared = sum_of_squares(c) % K
    if sum_squared > max_sum:
        max_sum = sum_squared

print(max_sum)
