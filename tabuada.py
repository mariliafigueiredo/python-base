#%%
"""Imprime a tabuada do 1 ao 10. """
_version_ = "0.1.1"
_author_ = "Marília"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorriveis)

# para cada numero em numeros:
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("--------------")
    print("-" * 10)


# %%
#%%
"""Imprime a tabuada do 1 ao 10. """
_version_ = "0.1.1"
_author_ = "Marília"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorriveis)

# para cada numero em numeros:
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} X {n2} = {resultado}"))
    print("#" * 18)

# %%