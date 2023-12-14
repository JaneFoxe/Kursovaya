import json


def load_data(load_path):
    with open(load_path, "r", encoding="UTF8") as file:
        list_dict = json.load(file)
    return list_dict


def selection_list(list_dict):
    result_list = []
    for item in list_dict:
        if item == {}:
            continue
        elif item['state'] == 'EXECUTED':
            result_list.append(item)
    return result_list




def sort_and_choice_list(list_dict):
    sorted_list = sorted(list_dict, key=lambda item: item['date'], reverse=True)
    return sorted_list[:5]


def date_transformation(date):
    stage_1 = date.split("T")[0]
    stage_2 = stage_1.split("-")
    total_stage = ".".join(stage_2[::-1])
    return total_stage


def account_number_transformation(num):
    if num == "Внесение наличных средств":
        return num
    elif "Счет" in num:
        return f"Счет **{num[-4:]}"
    else:
        return f"{num[:-16]}{num[-16:-12]} {num[-12:-10]}** **** {num[-4:]}"

#def output_result(list_dict):
#    for item in list_dict:
#        if 'from' in item:
#            print(f"{date_transformation(item['date'])} {item['description']}\n" \
#                  f"{account_number_transformation(item['from'])} -> {account_number_transformation(item['to'])}\n" \
#                  f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")
#        else:
#            print(f"{date_transformation(item['date'])} {item['description']}\n" \
#                  f"Внесение наличных средств -> {account_number_transformation(item['to'])}\n" \
#                  f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")


