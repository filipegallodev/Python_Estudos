from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome("C://Users/Filipe/OneDrive/Documentos/Python/selenium/chromedriver.exe")

navegador.get("https://www.google.com.br/")
time.sleep(1)

input_pesquisa = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_pesquisa.send_keys('sao paulo previsao do tempo' + Keys.ENTER)
time.sleep(5)

input_pesquisa = navegador.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
input_pesquisa.clear()
input_pesquisa.send_keys('americana previsao do tempo' + Keys.ENTER)
time.sleep(5)
