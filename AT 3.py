ano09=0
ano19=0
mediabbt = 0
mediabbt1 = 0
mediabb = 0
mediabb1 = 0
mediafrie = 0
mediafrie1 = 0
mediablack = 0
mediablack1 = 0
quantbbt = 0
quantbb = 0
quantfrie = 0
quantblack = 0
def verificar_ano(data):
    ano=int(data[-2]+data[-1])
    return ano


with open('series.csv', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        
        div = line.split(',')
        if int(div[5]) == 10 and int(div[6])==10:
            print('Série: ', div[0])
            print('Episódio: Temporada {}, Ep {}'.format(div[1], div[2]))
            print('Nota IMDB: ', div[5])
            print('Nota Netflix: ', div[6])
       
        ano = verificar_ano(div[3])
        
        if int(ano)>=10 and int(ano)<=19:
           ano19 = ano19 + 1
        else:
            ano09 = ano09 + 1

         
     
        if div[0] == 'The Big Bang Theroy':
            media += int(div[5])
            media += int(div[6])
            quant += 1
        elif div[0] == 'Friends':
            mediafrie += int(div[5])
            mediafrie1 += int(div[6])
            quantfrie += 1
        elif div[0] == 'Breaking Bad':
            mediabb += int(div[5])
            mediabb1 += int(div[6])
            quantbb += 1
        elif div[0] == 'Black Mirror':
            mediablack += int(div[5])
            mediablack1 += int(div[6])
            quantblack+= 1

    print('Número de episódios até 2009: ', ano09)
    print('Número de episódios entre 2010 e 2019: ', ano19)
    print()
    print('Black Mirror:         {}(IMDB)  {}(Netflix)'.format(round(mediablack/quantblack, 2), round(mediablack1/quantblack, 2)))
    print('Breaking Bad:         {}(IMDB)  {}(Netflix)'.format(round(mediabb/quantbbt, 2), round(mediabb1/quantbbt, 2)))
    print('The Big Bang Theory:  {}(IMDB)  {}(Netflix)')
    print('Friends:              {}(IMDB)  {}(Netflix)'.format(round(mediafrie/quantfrie, 2), round(mediafrie1/quantfrie, 2)))
    
