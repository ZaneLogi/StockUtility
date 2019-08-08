import requests
import datetime
import locale
import json

def get_stock_history(date, stock_no):
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s' % ( date, stock_no)
    r = requests.get(url)
    data = r.json()
    return transform(data)
    
def transform(data):
    if data['stat'] == 'OK':
        list = [transform_item(d) for d in data['data']]
        return list
    else:
        return []

def transform_item(data):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    item = {}
    item['date'] = data[0]
    item['trade_volume'] = locale.atoi(data[1])
    item['transaction'] = locale.atoi(data[2])
    item['opening_price'] = locale.atof(data[3])
    item['highest_price'] = locale.atof(data[4])
    item['lowest_price'] = locale.atof(data[5])
    item['closing_price'] = locale.atof(data[6])
    item['diff'] = 0.0 if data[7] == 'X0.00' else locale.atof(data[7])
    return item

def transform_date(date):
    y, m, d = date.split('/')
    return str(int(y)+1911) + '/' + m  + '/' + d

def write_json_file(filename, data_list):
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data_list, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))

def read_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as json_file:
            data = json_file.read()
            return json.loads(data)
    except EnvironmentError:
        return []

if __name__ == '__main__':
    history = get_stock_history("20190801", '2330')
    write_json_file('2330.json', history)

    
