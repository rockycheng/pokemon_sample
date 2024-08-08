import requests

def get_the_status_code(test_api_url):
    return requests.get(test_api_url).status_code

def get_the_API_data(test_api_url):
    headers_data = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"}
    url = test_api_url
    response = requests.get(url, headers=headers_data)
    #print(response.request.headers)
    #print(response.request.url)
    return response.json()

def get_pockmon_name(jsonDatas):
    #print(jsonDatas['name'])
    return jsonDatas['name']

def get_pockmon_type(jsonDatas):
    # print(jsonDatas['types'])
    type_list = []
    for type_info in jsonDatas['types']:
        type_info = type_info['type']['name']
        type_list.append(type_info)
    # print(type_list)
    return type_list

def get_pockmon_weight(jsonDatas):
    return jsonDatas['weight']

def get_pockmon_item_count(jsonDatas):
    return jsonDatas['count']

def get_pockmon_item_cost(jsonDatas):
    return jsonDatas['cost']