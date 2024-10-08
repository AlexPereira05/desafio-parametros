def rankeada(vitoria, derrotas):

  vitorias = int(vitoria - derrotas)

  if vitorias <= 10 :
    rank = "Ferro"
  elif vitorias <= 20:
    rank = "Bronze"
  elif vitorias <= 50:
    rank = "Prata"
  elif vitorias <= 80:
    rank = "Ouro"
  elif vitorias <= 90:
    rank = "Diamante"
  elif vitorias <= 100:
    rank = "Lendário"
  elif vitorias >= 101:
    rank = "Imortal"
  

  print(f"O Herói tem {vitorias} vitórias e está no nível {rank} ")

while True:

    saldoVitorias = int(input("Digite o número de vitórias: "))
    saldoDerrotas = int(input("Digite o número de derrotas: "))

    rankeada(saldoVitorias, saldoDerrotas)
