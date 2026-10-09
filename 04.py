import math

# Kör kerület és területe
# Kerület = 2 * r * pi
# Terület = r * r * pi == r2 * pi
# pi=3.15

atlo = 7
sugar = atlo / 2
# pi = 3.14
pi = math.pi

kerulet = (sugar * 2)  * pi
# terulet = (sugar * sugar) * pi
# terulet = (sugar ** 2) * pi
terulet = math.pow(sugar, 2) * pi

print(f'A kör kerülete: {kerulet:.2f}cm és területe {terulet:.3f}cm2. ')


