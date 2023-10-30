
class LoginPage:

    def __init__(self, page) -> None:
        # Inicjacja obiektów, przycisków na stronie logowania
        self.page = page
        self.email = page.get_by_placeholder("E-Mail Address")
        self.password = page.get_by_placeholder("Password")
        self.submit_btn = page.get_by_role("button", name="Login")
        self.forgotten_pass = page.locator("#form-login").get_by_role("link", name="Forgotten Password")

    def fillout_form(self, email_str, password_str):
        self.email.fill(email_str)
        self.password.fill(password_str)

    def submit_click(self) -> None:
        self.submit_btn.click()

    def forgotten_password(self) -> None:
        self.forgotten_pass.click()

    def loginpage_run(self)-> None:
        self.page.goto("https://demo.opencart.com/index.php?route=account/login&language=en-gb")