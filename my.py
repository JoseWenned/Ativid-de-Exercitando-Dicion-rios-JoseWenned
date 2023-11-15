d1 = {"name": "Kenzinho", "cidade": "Curitiba", "modulo": "M5"}

# Function 1

print(d1["name"])


# Function 2

print(d1["cidade"])

# Function 3

print(d1["modulo"])


# Function 4


print(d1.get("telegone", "a chave telefone não existe"))


# Function 5

for chave in d1.keys(): 
    print(chave)

# Function 6

for values in d1.values(): 
    print(values)


# Function 7

lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["999-999-999", False, 28]

print(f"chave:{lista_1}, values:{lista_2}")

# Function 8

lista_1 = (["999-999-999", False, 28])
print(lista_1)

# Function 9


# Function 10

d1.clear()
print(d1)