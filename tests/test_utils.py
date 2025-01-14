import pytest
import json

import datetime
import datetime as dt
import unittest
from pathlib import Path
from unittest.mock import Mock, mock_open, patch

import pandas as pd
import pytest

from src.utils import read_json_data, create_category_from_json
from src.settings import BASE_DIR
json_filename = Path(BASE_DIR, "data", "products.json")


class TestReadJsonData(unittest.TestCase):
    @patch(
        "builtins.open",
        mock_open(
            read_data="""
    {"name": "Телевизоры",
     "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
      "products": 
      [
      {"name": "55' QLED 4K",
       "description": "Фоновая подсветка",
        "price": 123000.0,
         "quantity": 7}
         ]
         }
    """
        ),
    )
    def test_read_json_data(self):
        products = read_json_data("path/to/file.json")
        self.assertEqual(
            products,
            {"name": "Телевизоры",
             "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
             "products":
                 [
                     {"name": "55' QLED 4K",
                      "description": "Фоновая подсветка",
                      "price": 123000.0,
                      "quantity": 7}
                 ]
             },
        )

    @patch(
        "builtins.open",
        mock_open(
            read_data="""
    {
        "user_currencies": [],
        "user_stocks": []
    }
    """
        ),
    )
    def test_read_json_data_empty(self):
        data = read_json_data("path/to/file.json")
        self.assertEqual(data, {"user_currencies": [], "user_stocks": []})


    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_json_data_file_not_found(self, mock_open):
        with self.assertRaises(FileNotFoundError):
            read_json_data("path/to/file.json")


def test_create_category_from_json_obj_category(data_test):
    result = create_category_from_json(data_test)
    assert len(result) == 2


def test_create_category_from_json_obj_product(data_test):
    result = create_category_from_json(data_test)

    assert len(result[0].products) == 3


