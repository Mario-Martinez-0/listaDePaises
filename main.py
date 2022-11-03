
numeroPais = int(input("Ingrese el numero de pais: "))
pais = []

for i in range(0, numeroPais):
    paises = input(f'ingrese el pais N°{i + 1},' )
    pais.append(paises)
    repetido = set(pais)
    ordenado = sorted(repetido)

print(ordenado)



