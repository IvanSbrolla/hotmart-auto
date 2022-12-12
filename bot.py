import math
import os
import dialog as Dialog
from webPage import WebPage

from hotmart import Hotmart
from product import Product
from filters import Filter

from time import sleep

os.system('cls')
products: list[Product] = []
optn_filter_temperature = False
optn_filter_count_rating = False
optn_filter_comission = False

user_email = Dialog.getEmail()
user_pwd = Dialog.getPwd()
filter = Dialog.getFilter()

optn = Dialog.getOptn('Deseja utilizar filtro de comissão? ( s/n ): ')
if optn.lower() == 's':
    comission = Dialog.getComission()
    optn_filter_comission = True

optn = Dialog.getOptn('Deseja utilizar filtro de quantidade de avaliação? ( s/n ): ')
if optn.lower() == 's':
    count_rating = Dialog.getCountRating()
    optn_filter_count_rating = True

optn = Dialog.getOptn('Deseja utilizar filtro de temperatura? ( s/n ): ')
if optn.lower() == 's':
    temperature = Dialog.getTemperature()
    optn_filter_temperature = True

optn = Dialog.getOptn('Deseja utilizar limite de buscas? ( s/n ): ')
if optn.lower() == 's':
    limit_count_result = Dialog.getLimitCountResult()
    optn_filter_limit_count_result = True

file_name = Dialog.getFileName()

webpage = WebPage()
driver = webpage.getDriver()
hotmart = Hotmart(user_email, user_pwd, filter, driver)
try:
    hotmart.resumeInit()
except:
    print(f'[ ! ] Falha ao se conectar na plataforma! Tentando novamente. Por favor, aguardo um instante...')
    driver.close()
    driver = webpage.getDriver()
    hotmart = Hotmart(user_email, user_pwd, filter, driver)
    hotmart.resumeInit()


hotmart.filter()

count_result = hotmart.getCountResult()
count_result = int(hotmart.clearStrCountResult(count_result))

aux_count_cards = 1
for number_page in range(0, math.ceil(count_result / 20)):  # percorre as paginas
    cards = hotmart.getCards()
    for card in cards:  # percorre os cards pegando as informações
        body_card = hotmart.getBodyCard(card)
        comission_card = hotmart.getComissionCard(body_card)
        comission_card = hotmart.formatComissionCard(comission_card)
        url_card = hotmart.getUrlCard(card)
        rating_card = hotmart.getRatingCard(body_card)
        count_rating_card = hotmart.getCountRatingCard(body_card)
        count_rating_card = hotmart.formatCountRating(count_rating_card)
        temperature_card = hotmart.getTemperatureCard(body_card)
        temperature_card = hotmart.formatTemperatureCard(temperature_card)
        name_card = hotmart.getNameCard(body_card)

        product = Product(name_card, url_card, comission_card, rating_card,
                          count_rating_card, temperature_card)
        products.append(product)
        print(f'[ + ] {aux_count_cards} "{product.name.upper()}" Add to list.')

        if optn_filter_limit_count_result == True and limit_count_result == aux_count_cards:
            break
        aux_count_cards += 1
    if optn_filter_limit_count_result == True and limit_count_result == aux_count_cards:
        break
    else:
        hotmart.nextPage()
    sleep(1)

if optn_filter_comission == True:  # Filtra comissao
    aux: list[Product] = []
    print('\n[ ~ ] FILTRANDO COMISSÃO!')
    print('---------------------------------------------')
    for product in products:
        if Filter(product.comission, comission).filterASC():
            aux.append(product)
            print(
                f'[ + ] COMISSÃO: R${product.comission:.2f} | "{product.name.upper()}" | {product.url}')
    print('---------------------------------------------')
    products = aux

if optn_filter_count_rating == True:  # Filtra quantidade de avaliações
    aux: list[Product] = []
    print('\n[ ~ ] FILTRANDO QUANTIDADE DE AVALIAÇÕES!')
    print('---------------------------------------------')
    for product in products:
        if Filter(int(product.count_rating), count_rating).filterASC():
            aux.append(product)
            print(
                f'[ + ] QNTD. AVALIAÇÃO: ({product.count_rating}) | "{product.name.upper()}" | {product.url}')
    print('---------------------------------------------')
    products = aux

if optn_filter_temperature == True:  # Filtra temperatura
    aux: list[Product] = []
    print('\n[ ~ ] FILTRANDO TEMPERATURA!')
    print('---------------------------------------------')
    for product in products:
        if Filter(temperatures=[int(temperature[0]),int(temperature[1])], productValue=product.temperature).filterTemperature():
            aux.append(product)
            print(
                f'[ + ] TEMPERATURA: {product.temperature}° | "{product.name.upper()}" | {product.url}')
    print('---------------------------------------------')
    products = aux

list_txt = open(file_name, 'a', encoding='utf-8')
aux_count_products = 1
for product in products:
    list_txt.write(
        f'~> [{aux_count_products}] | COMISSAO : R${product.comission:.2f} | QUANTIDADE DE AVALIAÇÕES : {product.count_rating} | TEMPERATURA : {product.temperature} | "{product.name.upper()}" | {product.url} \n')
list_txt.close()
print(f'\n[ + ] Arquivo {file_name.upper()} gerado com sucesso!')

print('\n[ ! ] Busca realizada com exito! Encerrando sistema...')
exit()
