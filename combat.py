import create_char
import create_enemy

char = create_char
enemy = create_enemy

print(char.sts_str)
print(enemy.sts_str)

while char.sts_vit > 0 or enemy.sts_vit > 0 :
    print(f'Vida char: {char.sts_vit}')
    print(f'Vida enemy: {enemy.sts_vit}')
    print("Char atacou")
    enemy.sts_vit -= char.sub_sts_atq
    print("Enemy atacou")
    char.sts_vit -= enemy.sub_sts_atq

    if char.sts_vit <= 0:
        print("Enemy ganhou")
        char.sts_vit = 0
        break
    elif enemy.sts_vit <= 0:
        print("Char ganhou")
        enemy.sts_vit = 0
        char.exp_bar += 10
        break

print(f'Char life: {char.sts_vit} \n exp: {char.exp_bar}')
print(f'Enemy life: {enemy.sts_vit}')

