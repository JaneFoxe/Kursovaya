
from random import randint
from src import utils

def test_load_data(fixture):
    assert type(fixture) == list
    assert type(fixture[randint(0, len(fixture))]) == dict


def test_selection_list(items):
    assert utils.selection_list(items) == [{
    "id": 957763565,
    "state": "EXECUTED",
    "date": "2019-01-05T00:52:30.108534",
    "operationAmount": {
      "amount": "87941.37",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 46363668439560358409",
    "to": "Счет 18889008294666828266"
  }]

def test_sort_and_choice_list(input_data):
    expected_result = [{'date': '2022-05-01'}, {'date': '2022-04-01'}, {'date': '2022-03-01'}, {'date': '2022-02-01'}, {'date': '2022-01-01'}]

    assert utils.sort_and_choice_list(input_data) == expected_result


def test_date_transformation():
    assert utils.date_transformation("2018-03-09T23:57:37.537412") == "09.03.2018"
    assert utils.date_transformation("2019-05-19T12:51:49.023880") == "19.05.2019"
    assert utils.date_transformation("") == ""


def test_account_number_transformation():
    assert utils.account_number_transformation("MasterCard 6783917276771847") == "MasterCard 6783 91** **** 1847"
    assert utils.account_number_transformation("Счет 58518872592028002662") == "Счет **2662"
    assert utils.account_number_transformation("МИР 2956603572573342") == "МИР 2956 60** **** 3342"
    assert utils.account_number_transformation("Maestro 8602249654751155") == "Maestro 8602 24** **** 1155"





