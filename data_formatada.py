from datetime import datetime
import abc

class DataFormatada(abc.ABC):

    def data_hora():
        data = str(datetime.now())
        return f'{data[8:10]}/{data[5:7]}/{data[0:4]} {data[11:16]}'

    def hora():
        data = str(datetime.now())
        return f'{data[11:16]}'

    def data():
        data = str(datetime.now())
        return f'{data[8:10]}/{data[5:7]}/{data[0:4]}'

    def dia():
        data = str(datetime.now())
        return f'{data[8:10]}'

    def mes():
        data = str(datetime.now())
        return f'{data[5:7]}'

    def ano():
        data = str(datetime.now())
        return f'{data[0:4]}'

    def nome_mes(mes=None):
        if mes == None:
            data = str(datetime.now())
            mes = data[5:7]

        if mes == '01':
            return 'Janeiro'
        elif mes == '02':
            return 'Fevereiro'
        elif mes == '03':
            return 'Março'
        elif mes == '04':
            return 'Abril'
        elif mes == '05':
            return 'Maio'
        elif mes == '06':
            return 'Junho'
        elif mes == '07':
            return 'Julho'
        elif mes == '08':
            return 'Agosto'
        elif mes == '09':
            return 'Setembro'
        elif mes == '10':
            return 'Outubro'
        elif mes == '11':
            return 'Novembro'
        else:
            return 'Dezembro'

    def eh_bissexto(ano):
        ano = int(ano)
        if ano % 4 == 0:
            return True
        else:
            return False

"""
if __name__ == '__main__':
    #print(f'{dia()}/{mes()}/{ano()}')
    #print(nome_mes())
    #print(formatacao.eh_bissexto(2024))
"""
