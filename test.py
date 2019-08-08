import requests
import json
import locale
from bs4 import BeautifulSoup


def getList():
    url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    r = requests.get(url, stream=True)
    s = b''
    count = 0
    for chunk in r.iter_content(1024):
        try:
            s = chunk
        except:
            return s
        count = count + 1
        print(count)
        if count >= 700: break
    return s

def getTWSEdata(stockCode="1301", monthDate="20170801"):    
    r = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={}&stockNo={}'.format(monthDate,stockCode))
    j = json.loads(r.text)
    return j
'''
j = getTWSEdata()
print(j['fields'])
print(j['data'])
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
print(locale.atoi(j['data'][0][1]))
print(locale.atoi(j['data'][0][2]))
print(float(j['data'][0][7]))
print(float(j['data'][1][7]))
'''
