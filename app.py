# Nome do aparelho
nome_aparelho = input("Digite o nome do aparelho: ")

# Potência em watts
potencia = float(input("Digite a potência do aparelho: "))

# Tempo médio de uso diário em horas
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Consumo mensal em kWh/mês 
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Resultado:
print(f"Resultado")
print(f"Aparelho: {nome_aparelho}")
print(f"Potência: {potencia} ")
print(f"Uso diário: {horas_dia} horas")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")