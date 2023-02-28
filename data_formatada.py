from datetime import datetime
import abc

class DataFormatada(abc.ABC):

    def data_hora(segundos=False):
        data = str(datetime.now())
        if segundos == False:
            return f'{data[8:10]}/{data[5:7]}/{data[0:4]} {data[11:16]}'
        else:
            return f'{data[8:10]}/{data[5:7]}/{data[0:4]} {data[11::]}'

    def hora():
        data = str(datetime.now())
        return f'{data[11:16]}'

    def minutos():
        data = str(datetime.now())
        return f'{data[14:16]}'

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

    def nome_mes(mes=None,abreviacao=False):
        if mes == None:
            data = str(datetime.now())
            mes = data[5:7]

        if mes == '01':
            if abreviacao == False:
                return 'Janeiro'
            else:
                return 'jan'
        elif mes == '02':
            if abreviacao == False:
                return 'Fevereiro'
            else:
                return 'fev'
        elif mes == '03':
            if abreviacao == False:
                return 'Março'
            else:
                return 'mar'
        elif mes == '04':
            if abreviacao == False:
                return 'Abril'
            else:
                return 'Abr'
        elif mes == '05':
            if abreviacao == False:
                return 'Maio'
            else:
                return 'maio'
        elif mes == '06':
            if abreviacao == False:
                return 'Junho'
            else:
                return 'jun'
        elif mes == '07':
            if abreviacao == False:
                return 'Julho'
            else:
                return 'jul'
        elif mes == '08':
            if abreviacao == False:
                return 'Agosto'
            else:
                return 'ago'
        elif mes == '09':
            if abreviacao == False:
                return 'Setembro'
            else:
                return 'set'
        elif mes == '10':
            if abreviacao == False:
                return 'Outubro'
            else:
                return 'out'
        elif mes == '11':
            if abreviacao == False:
                return 'Novembro'
            else:
                return 'nov'
        elif mes == '12':
            if abreviacao == False:
                return 'Dezembro'
            else:
                return 'dez'
        else:
            return 'ano invalido!'

    def eh_bissexto(ano):
        ano = int(ano)
        if ano % 4 == 0:
            return True
        else:
            return False
    
    # esta função deve receber duas datas e retornar a quantidade de dias dentro do intervalo das datas
    def quantidade_dias(inicio,fim):
        pass

"""
if __name__ == '__main__':
    #print(f'{dia()}/{mes()}/{ano()}')
    #print(nome_mes())
    #print(formatacao.eh_bissexto(2024))
"""
