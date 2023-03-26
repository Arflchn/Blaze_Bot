import requests
x = requests.get('https://blaze.com/api/roulette_games/recent')
id_blaze = x.text[8:18]
roll = []
w = 0
r = 0
b = 0
while True:
    x = requests.get('https://blaze.com/api/roulette_games/recent')
    number = x.text[77:79]
    if x.text[78] == ',':
        number = x.text[77]
    id_now = x.text[8:18]
    if id_now != id_blaze:
        color = x.text[68]
        if color == '0':
            print(f'CAIU BRANCO N:{number}')
            roll.insert(0, 'BRANCO')
            w += 1
            r = 0
            b = 0
        if color == '1':
            print(f'CAIU VERMELHO N:{number}')
            roll.insert(0, 'VERMELHO')
            r += 1
            w = 0
            b = 0
        if color == '2':
            print(f'CAIU PRETO N:{number}')
            roll.insert(0, 'PRETO')
            b += 1
            w = 0
            r = 0
        print(roll)
        if w >= 2:
            print(f'BRANCO {w} VEZES SEGUIDAS')
            print(f'POSSIBILIDADE DE BRANCO NA PRÓXIMA É DE {(0.066 ** (w+1)) * 100:.2f}%')
        if r >= 2:
            print(f'VERMELHO {r} VEZES SEGUIDAS')
            print(f'POSSIBILIDADE DE VERMELHO NA PRÓXIMA É DE {(0.466 ** (r+1)) * 100:.2f}%')
        if b >= 2:
            print(f'PRETO {b} VEZES SEGUIDAS')
            print(f'POSSIBILIDADE DE PRETO NA PRÓXIMA É DE {(0.466 ** (b+1)) * 100:.2f}%')
    id_blaze = x.text[8:18]