# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

print("="*5, "Conversor de Temperatura: Celsius -> Fahrenheit", "="*5)

c = int(input("Informe a temperatura (°C): "))

print(f"A temperatura em Fahrenheit é {9*c/5 + 32:.0f}°F")