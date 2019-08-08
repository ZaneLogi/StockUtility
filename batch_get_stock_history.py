import time
from build_stock_ids_json import *
from get_stock_history import *

def get_stock_prices(stock_no, start_year, start_month, end_year, end_month, sleep_time=10):
    print(stock_no)
    month = start_month
    year = start_year
    result = []
    while (True):
        date_string = '{}{:0>2d}01'.format(year, month)
        print(date_string, end = '')
        history = get_stock_history(date_string, stock_no)
        print(' done')
        result.extend(history)
        month += 1
        if month > 12:
            month = 1
            year += 1
        if (year > end_year or (year == end_year and month > end_month)):
            break
        time.sleep(sleep_time)
    return result

def merge_prices(old_list, new_list):
    # convert old_list to the dict type with the date as the key
    dict_list = dict((old_list[i]['date'], old_list[i])for i in range(0, len(old_list)))
    # add new_list to the dict object just created using the date as the key
    for e in new_list:
        dict_list[e['date']] = e
    price_list = []
    # do sorting on the keys of dict_list
    keys = [*dict_list]
    list.sort(keys)
    # add the data to price_list based on the order of the keys
    for k in keys:
        price_list.append(dict_list[k])
    return price_list

def batch_get_stock_prices(stock_no_list, start_year, start_month, end_year, end_month, sleep_time=10):
    for stock_no in stock_no_list:
        history = read_json_file('stock_data/' + stock_no + '.json')
        new_data = get_stock_prices(stock_no, start_year, start_month, end_year, end_month, sleep_time)
        data_list = merge_prices(history, new_data) 
        write_json_file('stock_data/' + stock_no + '.json', data_list)
        if stock_no !=  stock_no_list[len(stock_no_list)-1]:
            time.sleep(sleep_time)
        
if __name__ == '__main__':
    all_stock_list = load_stock_ids_from_json('stock_ids.json')
    stock_category_list = category_ids(all_stock_list, 'Industrial_Group')
    stock_list = collect_stock_list(stock_category_list['其他業'])
    #batch_get_stock_prices(stock_list, 2018, 8, 2018, 8)
    #batch_get_stock_prices(['9945'], 2018, 1, 2018, 2)
    

    
