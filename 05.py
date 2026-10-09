vezeteknev = input('Add meg a vezetékneved: ')
utonev = input('Add meg az utóneved: ')
#eletkor = input('Add meg az életkorod évben: ')
szuletEv = input('Add meg a szüetési éved: ')

# print(f'A te neved: {vezeteknev} {utonev}, és {eletkor} éves vagy.')
print(f'A te neved: {vezeteknev} {utonev}, és {szuletEv}-ban/ben születtél.')
print(type(vezeteknev))
print(type(utonev))
print(type(szuletEv))

szuletEv = int(szuletEv)
print(type(szuletEv))

eletkor = 2026 - szuletEv 
print(f'Az életkorod {eletkor}')

