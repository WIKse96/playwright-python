


class AdminPage:
    def __init__(self, page) -> None:
        self.page = page
        self.url = 'https://demo.opencart.com/admin'
        self.login_btn = page.get_by_role("button", name=" Login")
        self.username_input = page.locator("xpath=//input[@id='input-username']")
        self.password_input = page.locator("xpath=//input[@id='input-password']")
        self.closepopup_btn = page.locator("xpath=//button[@class='btn-close']")
        self.system_btn = page.get_by_role("link", name=" System ")
        self.edit = page.get_by_label("Edit")
        self.metatitle_input = page.get_by_placeholder("Meta Title")
        self.save_btn = page.get_by_label("Save")
    def admin_run(self):
        self.page.goto(self.url)

    def fillOutForm(self, user, passw):
        self.username_input.fill(user)
        self.password_input.fill(passw)
        self.login_btn.click()

    def mainpanel(self):
        self.closepopup_btn.click()
        self.system_btn.click()
        self.edit.click()
        self.metatitle_input.fill("sklep")
        self.save_btn.click()


