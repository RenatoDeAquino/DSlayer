from os import stat
import random
name = input("Digite o nome do seu personagem\n>")

status = {
    'força':        random.randint(1, 10),
    'agilidade':    random.randint(1, 10),
    'destreza':     random.randint(1, 10),
    'respiração':   0,
    "vitalidade":   random.randint(1, 10)
}

inventario = {
    "armas": [],
    "utilitarios": [],
    "moedas": 10
}

print(f'seja bem vindo {name} seus status são')

for x in status:
    print(x, status[x])