from DOMs.login_page import LoginPage


class Test_login:

    def login_init(self, my_page):
        self.login_page = LoginPage(my_page)
        return self.login_page


    def test_login(self, my_page):
        self.login_init(my_page).fillout_form('wiktor.wiktor@op.pl', 'dupaDupowska1')