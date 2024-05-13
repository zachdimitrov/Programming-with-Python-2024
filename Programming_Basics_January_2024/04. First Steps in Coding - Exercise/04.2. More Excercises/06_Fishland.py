skumria = float(input('Skumria price: '))
tsatsa = float(input('Tsatsa price: '))
palamud_kg = float(input('Kg of palamud: '))
safrid_kg = float(input('Kg of safrid: '))
midi_kg = float(input('Kg of midi: '))
palamud = skumria + skumria * 0.6
safrid = tsatsa + tsatsa * 0.8
print(f'{palamud * palamud_kg + safrid * safrid_kg + 7.5 * midi_kg:.2f}')
