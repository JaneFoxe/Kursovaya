import pytest
from src import utils
from config import LOAD_DATA_PATH
@pytest.fixture
def fixture():
    return utils.load_data(f"../{LOAD_DATA_PATH}")

@pytest.fixture
def items():
    return [{
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
  },
        {
    "id": 27192367,
    "state": "CANCELED",
    "date": "2018-12-24T20:16:18.819037",
    "operationAmount": {
      "amount": "991.49",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 71687416928274675290",
    "to": "Счет 87448526688763159781"
  }, {}]

@pytest.fixture
def input_data():
    return [{'date': '2022-01-01'}, {'date': '2022-02-01'}, {'date': '2022-03-01'}, {'date': '2022-04-01'}, {'date': '2022-05-01'}]

