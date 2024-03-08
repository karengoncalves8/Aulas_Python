#  Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 

print("="*5, "Tempo de Viagem", "="*5)

d = int(input("Distância a percorrer (km): "))
vm = int(input("Velocidade média esperada (km/h): "))

print(f'O tempo viagem será de {d/vm:.1f} horas')