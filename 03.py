# Háromszög

# kerület = a + b + c

a_oldal = 6
b_oldal = 8
c_oldal = 9

kerulet_haromszog = a_oldal + b_oldal + c_oldal
#HERON képlet
#kerület fele --> s = ( a + b + c ) / 2   kerulet_haromszog/2

# Terulet = s * (s-a) * (s-b) * (s-c)  --ez a gyök alatt
s = kerulet_haromszog / 2

terulet_haromszog = (s * (s-a_oldal) * (s-b_oldal) * (s-c_oldal))**0.5

print(f"A háromszög kerülete: {kerulet_haromszog}cm, területe {terulet_haromszog}cm2")

# Számérték formázása f stringen belül
print(f"A háromszög kerülete: {kerulet_haromszog}cm, területe {terulet_haromszog:.2f}cm2")
