import json
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL
from utils.helpers import screenshot_path

with open("data/user.json") as file:
     USERS = json.load(file)

@pytest.mark.smoke
@pytest.mark.parametrize("user_key, expected_success", [
     ("valid", True),
     ("locked", False),
     ("invalid", False)
])
def test_login_variates(page, user_key, expected_success):
     login = LoginPage(page)
     inventory = InventoryPage(page)
     login.goto(BASE_URL)
     creds = USERS[user_key]
     login.login(creds["username"], creds["password"])