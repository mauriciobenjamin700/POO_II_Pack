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

    def quantidade_dias_mes(bissexto=False):
        if bissexto == False:
            jan = 31
            fev = 28
            mar = 31
            Abr = 30
            maio = 31
            jun = 30
            jul = 31
            ago = 31
            set = 30
            out = 31
            nov = 30
            dez = 31
            return [jan,fev,mar,Abr,maio,jun,jul,ago,set,out,nov,dez]
        else:
            jan = 31
            fev = 29
            mar = 31
            Abr = 30
            maio = 31
            jun = 30
            jul = 31
            ago = 31
            set = 30
            out = 31
            nov = 30
            dez = 31
            return [jan,fev,mar,Abr,maio,jun,jul,ago,set,out,nov,dez]


    def quantidade_dias(inicio,fim): # teste usando 12/09/2021 -> 15/10/2021
        #testar se estamos no mesmo ano e o inicio do intervalo e menor que o fim do intervalo
        if (int(inicio[6::])) == int(fim[6::]) & int(inicio[3:5]) == int(fim[3:5]):
            if int(inicio[0:2]) < int(fim[0:2]):

                #diferença de mês -> mes_final-mes_inicio -> 10-9 == 1
                dif_meses = int(fim[3:5]) - int(inicio[3:5])
                #diferença de dias -> dia_final - dia_inicial -> 15 - 12 == 3
                dif_dias = int(fim[0:2]) - int(inicio[0:2])

                return f'{(dif_meses*30)+dif_dias}' 

"""
if __name__ == '__main__':
    #print(f'{dia()}/{mes()}/{ano()}')
    #print(nome_mes())
    #print(formatacao.eh_bissexto(2024))
"""
