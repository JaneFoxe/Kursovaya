
from config import LOAD_DATA_PATH
from src import utils
from src.utils import date_transformation, account_number_transformation

if __name__ == '__main__':

    start_list = utils.load_data(LOAD_DATA_PATH)
    executed_list = utils.selection_list(start_list)
    sorted_list = utils.sort_and_choice_list(executed_list)






    def output_result(list_dict):
        for item in list_dict:
            if 'from' in item:
                print(f"{date_transformation(item['date'])} {item['description']}\n" \
                      f"{account_number_transformation(item['from'])} -> {account_number_transformation(item['to'])}\n" \
                      f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")
            else:
                print(f"{date_transformation(item['date'])} {item['description']}\n" \
                      f"Внесение наличных средств -> {account_number_transformation(item['to'])}\n" \
                      f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")


    output_result(sorted_list)
