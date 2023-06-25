import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.by import By
from ddt import ddt, data, file_data, unpack
import unittest
import allure
from allure_commons.types import AttachmentType
import pytest
import requests
import json
import jsonpath
import logging
import inspect
from openpyxl import load_workbook
import openpyxl
import csv