from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import pyperclip as pc
from time import sleep


class Hotmart:

    def __init__(self, user_email: str, user_pwd: str, filtro: str, driver: webdriver.Chrome):
        self.user_email = user_email
        self.user_pwd = user_pwd
        self.filtro = filtro
        self.driver = driver
        self.url_page = f'https://app-vlc.hotmart.com/market/'

    def goToPage(self):
        self.driver.get(self.url_page)
        sleep(1)

    def login(self):

        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        input_email_user = inputs[0]
        input_pwd_user = inputs[1]
        input_email_user.send_keys(self.user_email)
        input_pwd_user.send_keys(self.user_pwd)
        sleep(1)
        self.driver.execute_script(
            'document.getElementsByTagName("button")[2].click()')
        sleep(3)

    def resumeInit(self):
        self.goToPage()
        self.login()

    def filter(self):
        input_search = self.driver.execute_script(
            'return document.getElementById("app-market").shadowRoot.querySelectorAll("input")[1]')
        input_search.send_keys(self.filtro)
        sleep(1)
        input_search.send_keys(Keys.ENTER)
        sleep(2)

    def getCountResult(self):
        return self.driver.execute_script('return document.getElementById("app-market").shadowRoot.querySelectorAll(".hot-container")[2].querySelector("p").innerText')

    def clearStrCountResult(self, string):
        aux = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(0, len(aux)):
            string = string.replace(aux[i], '')
        return string

    def nextPage(self):
        self.driver.execute_script(
            'aux=document.getElementById("app-market").shadowRoot.querySelectorAll("hot-pagination-item");aux[aux.length-1].click()')

    def getCards(self):
        return self.driver.execute_script('return document.getElementById("app-market").shadowRoot.querySelectorAll(".hot-col-xl-3")')

    def getUrlCard(self, card: WebElement):
        tag_link = card.find_element(By.TAG_NAME, 'a')
        return tag_link.get_attribute('href')

    def getBodyCard(self, card: WebElement):
        return card.find_element(By.TAG_NAME, 'hot-card-body')

    def getRatingCard(self, bodyCard: WebElement):
        return bodyCard.find_elements(By.TAG_NAME, 'span')[0].text

    def getCountRatingCard(self, bodyCard: WebElement):
        return bodyCard.find_elements(By.TAG_NAME, 'span')[1].text

    def getTemperatureCard(self, bodyCard: WebElement):
        return bodyCard.find_elements(By.TAG_NAME, 'span')[2].text

    def getNameCard(self, bodyCard: WebElement):
        return bodyCard.find_elements(By.TAG_NAME, 'span')[3].text

    def getComissionCard(self, bodyCard: WebElement):
        return bodyCard.find_elements(By.TAG_NAME, 'p')[1].text

    def formatComissionCard(self, string: str):
        try:
            aux = 'R$ '
            if string.__contains__('.'):
                string = string.replace('.', '')
            for i in range(0, len(aux)):
                string = string.replace(aux[i], '')

            if string.__contains__(','):
                string = float(string.replace(',', '.'))
            string_format = "{:.2f}".format(string)
            return float(string_format)
        except:
            return 00.00

    def formatTemperatureCard(self, string: str):
        if string.__contains__('°'):
            string = string.replace('°', '')
            return int(string)
        else:
            return 0
    
    def formatCountRating(self, string:str):
        aux = "()"
        for i in range(0, len(aux)):
            string = string.replace(aux[i], '')
        return int(string)

