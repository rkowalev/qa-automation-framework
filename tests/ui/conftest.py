import pytest
from playwright.sync_api import Page
from pages.todo_page import TodoPage
from pages.login.login_page import LoginPage
from pages.login.secure_area_page import SecureAreaPage

@pytest.fixture
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def secure_area_page(page: Page):
    return SecureAreaPage(page)