import pytest

from DOMs.homepage import HomePage
from DOMs.categorypage import CategoryPage
from DOMs.login_page import LoginPage


def test_category(page) -> None:

    category_page = CategoryPage(page)
    category_page.category_open_by_menu()
    category_page.products_list_test()


def test_e2e(page) -> None:

    homepage = HomePage(page)
    homepage.homepage_run()
    homepage.login_run()



def test_login(page) -> None:
    login_page = LoginPage(page)
    login_page.loginpage_run()
    login_page.fillout_form("email@email", "dupadupadupa")
