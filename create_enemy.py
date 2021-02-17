import random

sts_str = random.randint(1, 10)
sts_agi = random.randint(1, 10)
sts_dex = random.randint(1, 10)
sts_vit = random.randint(50, 100)
sts_brf = random.randint(50, 100)

sub_sts_atq = sts_str + sts_dex / 2
sub_sts_def = (sts_vit/10) + sts_dex / 2
sub_sts_esq = sts_agi + sts_dex / 2


""" print(f'Força - str -> {sts_str}')
print(f'Agilidade - agi -> {sts_agi}')
print(f'Destreza - dex -> {sts_dex}')
print(f'Vitalidade - vit -> {sts_vit}')
print(f'Breath - brf -> {sts_brf}')
 """
