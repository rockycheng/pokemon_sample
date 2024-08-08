import json
import controller as controller

# loading config
with open('test_configure/config.json', 'r') as f:
    config_data = json.load(f)
# setup_config_data
host = config_data['test_server']['host']
pokemon_path = config_data['api_information']['pokemon_path']
pokemon_item_path = config_data['api_information']['pokemon_item_path']

# loading the test data
with open('test_scenarios/test_data.json', 'r') as f:
    test_data = json.load(f)

POKEMON_NAME = test_data['pokemon_name']
POKEMON_ID = test_data['pokemon_id']
POCKMON_ITEM_COUNT = test_data['pokemon_item_count_on_20240808']

# Testing the test server is ready. (200)
def test_01_pockmon_url_check_status_code_equals_200():
    api_url = host + pokemon_path
    response_status_code =controller.get_the_status_code(api_url)
    assert response_status_code == 200

# Confirm_the_pokemon_name
def test_02_confirm_the_pokemon_name():
    api_url = host + pokemon_path + POKEMON_ID
    actual_result = controller.get_pockmon_name(controller.get_the_API_data(api_url))
    print("")
    print('Id: 6, Pockmon Name:' + actual_result)
    assert actual_result == POKEMON_NAME

#列出 id < 20, id > 0 的寶可夢名稱（name）以及其寶可夢的屬性（types），依照 id 由小至大排序
def test_03_confirm_the_pokemon_list_order_by_id():
    pokemon_list = []
    for count in range(1, 19):
        api_url = host + pokemon_path + str(count)
        pockmon_id = count
        pockmon_name = controller.get_pockmon_name(controller.get_the_API_data(api_url))
        pockmon_type = controller.get_pockmon_type(controller.get_the_API_data(api_url))
        print("")
        print('Id: ' + str(pockmon_id) + ', Pockmon Name: ' + pockmon_name + ', Types: ' + str(pockmon_type))
        pokemon_list.append({"id": pockmon_id, "name": pockmon_name, "type": pockmon_type})

    assert pokemon_list == sorted(pokemon_list, key=lambda x: x['id'])

#列出 id < 100, id > 0 的寶可夢中，體重（weight） < 50 的寶可夢名稱（name）及寶可夢體重（weight），並且依照體重由大至小排序
def test_04_confirm_the_pokemon_list_order_by_weight():
    pokemon_list = []
    for count in range(1, 99):
        api_url = host + pokemon_path + str(count)
        pockmon_id = count
        pockmon_weight = controller.get_pockmon_weight(controller.get_the_API_data(api_url))
        if pockmon_weight < 50:
            pockmon_name = controller.get_pockmon_name(controller.get_the_API_data(api_url))
            pokemon_list.append({"id": pockmon_id, "name": pockmon_name, "weight": pockmon_weight})

    #reverse the pokemon_list
    pokemon_list_reverse = sorted(pokemon_list, key=lambda x: x['weight'], reverse=True)
    for pokemon_info in pokemon_list_reverse:
        print("")
        print('Id: ' + str(pokemon_info['id']) + ', Pockmon Name: ' + pokemon_info['name'] + ', Weight: ' + str(pokemon_info['weight']))

    assert pokemon_list_reverse == sorted(pokemon_list, key=lambda x: x['weight'], reverse=True)

# Testing the test server is ready. (200)
def test_05_pockmon_item_url_check_status_code_equals_200():
    api_url = host + pokemon_item_path
    response_status_code =controller.get_the_status_code(api_url)
    assert response_status_code == 200

#Check the pokemon item count
def test_06_confirm_the_pokemon_item_count():
    api_url = host + pokemon_item_path
    actual_result = controller.get_pockmon_item_count((controller.get_the_API_data(api_url)))
    print("")
    print('Pockmon Item Count: ' + str(actual_result))
    assert actual_result == POCKMON_ITEM_COUNT

#列出 id < 20, id > 0 的寶可夢物品名稱（name），依照 id 由小至大排序
def test_07_confirm_the_pokemon_item_list_order_by_id():
    pokemon_item_list = []
    for count in range(1, 19):
        api_url = host + pokemon_item_path + str(count)
        pockmon_id = count
        pockmon_item_name = controller.get_pockmon_name(controller.get_the_API_data(api_url))
        print("")
        print('Id: ' + str(pockmon_id) + ', Pockmon Item Name: ' + pockmon_item_name)
        pokemon_item_list.append({"id": pockmon_id, "name": pockmon_item_name})

    assert pokemon_item_list == sorted(pokemon_item_list, key=lambda x: x['id'])

#列出 id < 50, id > 0 的寶可夢物品中，價格（cost）≤ 1500 的寶可夢物品名稱（name）及寶可夢物品價格（cost），並且依照花費價格（cost）由大至小排序
def test_08_confirm_the_pokemon_item_list_order_by_cost():
    pokemon_item_list = []
    for count in range(1, 49):
        api_url = host + pokemon_item_path + str(count)
        pockmon_id = count
        pockmon_cost = controller.get_pockmon_item_cost(controller.get_the_API_data(api_url))
        if pockmon_cost <= 1500:
            pockmon_item_name = controller.get_pockmon_name(controller.get_the_API_data(api_url))
            pokemon_item_list.append({"id": pockmon_id, "name": pockmon_item_name, "cost": pockmon_cost})

    #reverse the pokemon_item_list
    pokemon_item_list_reverse = sorted(pokemon_item_list, key=lambda x: x['cost'], reverse=True)
    for pokemon_info in pokemon_item_list_reverse:
        print("")
        print('Id: ' + str(pokemon_info['id']) + ', Pockmon Item Name: ' + pokemon_info['name'] + ', Cost: ' + str(pokemon_info['cost']))

    assert pokemon_item_list_reverse == sorted(pokemon_item_list, key=lambda x: x['cost'], reverse=True)