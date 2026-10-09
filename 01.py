# print(valami)
# A négyzet oldalhosszúsága 4 cm 
# számold ki a kerületet és a területet

# változó
a_oldal = 4

# kerület : a + a + a + a  => 4*a
kerulet = 4 * a_oldal

print("A négyzet kerülete: ", end="")
#
#print(4*4)
#print(4*a_oldal)
print(kerulet)

#terület : a * a vagy a2(négyzet)
# terulet = 4 * 4 
# terulet = 4 ** 2 
# terulet = a_oldal * a_oldal

terulet = a_oldal ** 2 
print("A négyzet területe: ", end="")
print(terulet)

#f string
# string interpoláció

print(f"A négyzet kerülete: {kerulet} cm")
print(f"A négyzet területe: {terulet} cm2")