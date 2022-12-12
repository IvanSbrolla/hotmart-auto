from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebPage():
    def __init__(self) -> None:
        pass
    def getDriver(self):
        service = Service(executable_path='chromedriver.exe')
        chrome_options = Options()
        chrome_options.add_argument( "--log-level=3")
        return webdriver.Chrome(service=service, options=chrome_options)