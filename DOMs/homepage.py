from playwright.sync_api import expect


class HomePage:
    def __init__(self, page) -> None:
        # Inicjacja obiektów, przyciskow na stronie głównej
        self.page = page
        self.powered = page.get_by_text("Powered By OpenCart Your Store © 2023")
        self.cart_btn = page.get_by_role("button", name=" 0 item(s) - $0.00")
        self.pageTitle = "Your Store"
        self.logo_btn = page.get_by_role("link", name=self.pageTitle)
        self.software_menu = page.get_by_role("link", name="Software")
        self.main_menu = page.get_by_role("main")
        self.myAccount = page.get_by_role("link", name=" My Account ")
        self.login_btn = page.locator("xpath=//a[normalize-space()='Login']")


    def homepage_run(self) -> None:
        # Wykonywanie akcji, które uruchamiamy jako testy
        self.logo_btn.click()
        # asercje czy znajdujemy się na stronie glównej
        expect(self.page).to_have_title(self.pageTitle)
        expect(self.cart_btn)
        expect(self.powered)

    def login_run(self):
        self.myAccount.click()
        self.login_btn.click()
