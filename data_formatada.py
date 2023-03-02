from datetime import datetime
import abc

class DataFormatada(abc.ABC):
    """
    Uma classe voltada para trabalhar com datas/horas e suas peculiaridades

    ...

    Attributes
    ----------
   
    Methods
    -------
    data_hora(segundos=False):
        retorna uma string com a data e hora atuais
    hora():
        retorna uma string com a hora atual
    minutos():
        retorna uma string com os minutos atuais
    data():
        retorna uma string com a data atual
    dia():
        retorna uma string com o dia atual
    mes():
        retorna uma string com o mês atual
    ano():
        retorna uma string com o ano atual
    nome_mes(mes=None,abreviacao=False):
        retorna uma string com o nome do mês passado ou atual
    eh_bissexto(ano):
        retorna um booleano referente ao fato do ano ser ou não bissexto
    quantidade_dias_mes(bissexto=False):
        retorna uma lista com o total de dias de seu respectivo mês
    quantidade_dias(inicio,fim):
        retorna uma string com o total de dias contido entre duas datas
    """

    def data_hora(segundos=False):
        """
        Caso a função não receba parâmetro, a mesma retorna um string formatada com a data e hora atuais.
        ex: 02/03/2023 09:31
        Se receber um parâmetro True:

            parameters:
                numero {string} : numero da conta que se deseja buscar

            return:
            Tuple : tupla com o resultado da busca pela conta
        """
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
            maio= 31
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
        
        dia_inicio = int(inicio[0:2])
        mes_inicio = int(inicio[3:5])
        ano_inicio = int(inicio[6::])

        dia_fim = int(fim[0:2])
        mes_fim = int(fim[3:5])
        ano_fim = int(fim[6::])
        
        #se ano atual e igual a ano final
        if ano_inicio == ano_fim:
            # se mes atual é igual a mes final
            if mes_inicio == mes_fim:
                #se o dia atual é menor que o dia final
                if dia_inicio < dia_fim:

                    #diferença de dias -> dia_final - dia_inicial -> 15 - 12 == 3
                    dif_dias = dia_fim - dia_inicio

                    return f'{dif_dias}'
                elif dia_inicio == dia_fim:
                    return '0'

                else:
                    return 'Erro: A data final é menor que a data inicial'
            # se o mes atual é menor que o mes final
            elif mes_inicio < mes_fim:
                #criar um calendário baseado se o ano é bissexto ou não
                calendario = DataFormatada.quantidade_dias_mes(DataFormatada.eh_bissexto(ano_inicio))
                dias_restantes_mes_inicial = calendario[(mes_inicio-1)] - dia_inicio
                dias_necessarios_mes_final =  dia_fim

                #se houver apenas 1 mês de difernça
                if mes_fim - mes_inicio == 1:
                    return str(dias_restantes_mes_inicial + dias_necessarios_mes_final - 1)
                #se houver mais de 1 mês de diferença, precisamos descobrir quais são
                else:
                    total_dias = 0
                    for meses in range(mes_inicio,mes_fim+1):
                        total_dias += calendario[meses-1]

                    #funcionando, retorna o intervalo entre duas datas
                    return str(total_dias - dia_inicio - (calendario[mes_fim-1] - dias_necessarios_mes_final + 1))
                    
            else:
                return 'Erro: A data final é menor que a data inicial'

        elif ano_inicio < ano_fim:
            """
            se ano_final - ano_inicial == 1:
                para resolver o caso de uma diferença de anos, preciso concluir o ano inicial e pegar apenas o necessário do ano final.
            se ano_final - ano_inicial > 1:
                pegamos o resultado anterior e somamos com o total de dias no intervalo de anos  
            """                
            if ano_fim - ano_inicio == 1:
                #copiar e colar no elif de baixo 
                calendario = DataFormatada.quantidade_dias_mes(DataFormatada.eh_bissexto(ano_inicio))

                resto_mes_inicial = calendario[mes_inicio-1] - dia_inicio
                resto_ano_inicial = resto_mes_inicial + sum(calendario[mes_inicio:13])

                necessario_mes_final = dia_fim
                necessario_ano_final = necessario_mes_final + sum(calendario[0:mes_fim-2])

                #testar se o retorno está correto
                return str(resto_ano_inicial + necessario_ano_final)
            
            elif ano_fim - ano_inicio > 1:
                """
                para encontrar a diferença útil, precisamos achar a difereça de anos e reduzir os anos que não pegaremos todos os dias
                formula: ano final - ano inicial - 1
                """
                dias_intervalo_intocado = 0
                for ano in range(ano_inicio+1,ano_fim):
                    if DataFormatada.eh_bissexto(ano):
                        dias_intervalo_intocado+=366
                    else:
                        dias_intervalo_intocado += 365

                calendario = DataFormatada.quantidade_dias_mes(DataFormatada.eh_bissexto(ano_inicio))

                resto_mes_inicial = calendario[mes_inicio-1] - dia_inicio
                resto_ano_inicial = resto_mes_inicial + sum(calendario[mes_inicio:13])

                necessario_mes_final = dia_fim
                necessario_ano_final = necessario_mes_final + sum(calendario[0:mes_fim-2])

                #testar se o retorno está correto
                return str(resto_ano_inicial + necessario_ano_final+dias_intervalo_intocado)

        else:
            return 'Erro: A data final é menor que a data inicial'
