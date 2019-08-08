import csv
import json

def convert_stock_ids_from_csv_to_json(csv_filename, json_filename):
    csv_rows = []

    with open('stock_ids.txt', mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        title = reader.fieldnames
    
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])

    with open('stock_ids.json', mode='w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))


def load_stock_ids_from_json(json_filename):
    with open('stock_ids.json', 'r', encoding='utf-8') as myfile:
        data = myfile.read()
        return json.loads(data)

def category_ids(id_list, key_name):
    result = {}
    for i in id_list:
        if not (i[key_name] in result):
            result[i[key_name]] = []
        result[i[key_name]].append(i)
    return result

def collect_stock_list(ids, index_first = -1, index_last = -1):
    if index_first < 0:
        index_first = int(ids[0]['Code'])
    if index_last < 0:
        index_last = int(ids[len(ids) - 1]['Code'])
    result = []
    for i in ids:
        index = int(i['Code'])
        if index_first <= index and index <= index_last:
            result.append(i['Code'])
    return result

if __name__ == '__main__':
    #convert_stock_ids_from_csv_to_json('stock_ids.txt', 'stock_ids.json')
    all_stock_list = load_stock_ids_from_json('stock_ids.json')
    partial_stock_list = collect_stock_list(all_stock_list, 1000, 1200)
    print(partial_stock_list)
    stock_category_list = category_ids(all_stock_list, 'Industrial_Group')
    stock_list = collect_stock_list(stock_category_list['水泥工業'])
    print('Total stock count = ', len(all_stock_list))
    print(stock_category_list.keys())
    print(stock_list)



    

    

    

    








        

