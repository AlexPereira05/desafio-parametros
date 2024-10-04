#  Utilizei a função de input para o usuário selecionar o nome e quantidade de XP

nome_heroi = input("Digite o nome do herói: ")
xp_heroi = int(input("Digite a quantidade de XP do herói: "))

# Estrutura de decisão para determinar o nível do herói
if xp_heroi <= 1000:
    nivel = "Ferro"
elif xp_heroi <= 2000:
    nivel = "Bronze"
elif xp_heroi <= 5000:
    nivel = "Prata"
elif xp_heroi <= 7000:
    nivel = "Ouro"
elif xp_heroi <= 8000:
    nivel = "Platina"
elif xp_heroi <= 9000:
    nivel = "Ascendente"
elif xp_heroi <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"


print(f"O Herói de nome {nome_heroi} está no nível de {nivel}.")
