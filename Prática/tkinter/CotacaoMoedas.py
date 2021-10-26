import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: R$ {cotacao_dolar}
    Euro: R$ {cotacao_euro}
    BTC: R$ {cotacao_btc}'''

    textoCotacoes["text"] = texto


aplicacao = Tk()
aplicacao.title('Cotação Atual das Moedas')
aplicacao.geometry('400x200')

textoOrientacao = Label(aplicacao, text="Clique no botão para ver as cotações das moedas Dólar/Euro/BTC")
textoOrientacao.grid(column= 0, row= 0, padx=20, pady=10)

botaoCotacoes = Button(aplicacao, text="Buscar cotações", command=pegar_cotacoes)
botaoCotacoes.grid(column= 0, row= 1, padx=20, pady=10)

textoCotacoes = Label(aplicacao, text="")
textoCotacoes.grid(column= 0, row= 2, padx=20, pady=10)

aplicacao.mainloop()
