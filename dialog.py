import os
from getpass import getpass

def invalidValue(self):
    os.system('cls')
    print('\n[ ! ] Valor inserido incorreto. Tente novamente.')
    exit()

def getEmail():
    return input("\n[ + ] Insira o Email utilizado na Hotmart: ")

def getPwd():
    return getpass("\n[ + ] Insira a Senha utilizada na Hotmart: ")

def getFilter():
    return input("\n[ + ] Qual filtro (palavra-chave) deseja utilizar?: ")

def getComission():
    comission = input("\n[ + ] Comissão maior que (exmp: R$9999,99): R$")
    if comission.__contains__(','): comission = comission.replace(',', '.')
    comission = float(comission)
    if comission < 0 :
        invalidValue()
    else:
        return comission

def getCountRating():
    rating = input("\n[ + ] Quantidade de avaliações maior que: ")
    rating = int(rating)    
    if rating < 0 :
       invalidValue()
    else: 
        return rating

def getTemperature():
    temperature_max = input("\n[ + ] Temperatura (-)menor que: ")
    temperature_min = input("\n[ + ] Temperatura (+)maior que: ")
    temperature_max = int(temperature_max)
    temperature_min = int(temperature_min)
    if temperature_min < 0 or temperature_max < 0:
        invalidValue()
    else: 
        return [temperature_max,temperature_min]

def getLimitCountResult():
    limit_count_result = input("\n[ + ] Insira o limite de busca que deseja usar. (ex: 9, 99, 999, 9999...): ")
    limit_count_result = int(limit_count_result)
    if limit_count_result <= 0:
        invalidValue()
    else:
        return limit_count_result

def getFileName():
    file_name = input('\n[ + ] Insira um nome para o .txt! (padrao: "list.txt"): ')
    if file_name == None or file_name == '':
        return 'list.txt'
    if file_name.__contains__('.txt'):
        return file_name
    else:
        return file_name+".txt"

def getOptn(msg):
    return str(input(f'\n[ + ] {msg}'))
