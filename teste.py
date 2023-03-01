from data_formatada import DataFormatada
"""
ano = input('Digite um ano e eu te direi se ele é bissexto: ')
if ano.isnumeric():
    resultado = DataFormatada.eh_bissexto(ano)
    if resultado:
        print('o ano {ano} é Bissexto! ')
    else:
        print('o ano {ano} não é Bissexto! ')
else:
    print('Digite um ano corretamente')
"""

#print(f'Nos estamos no mês de {DataFormatada.nome_mes()}')

#print(f'Estamos neste momento na hora {DataFormatada.hora()}')

#print(DataFormatada.data_hora())
#print(DataFormatada.data_hora(True))

#print(DataFormatada.minutos())

#print(f'A diferença entre 12/09/2021 e 15/10/2021 é {DataFormatada.quantidade_dias("12/09/2021", "15/10/2021")}')

print(DataFormatada.quantidade_dias('01/03/2023','01/05/2023'))