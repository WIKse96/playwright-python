class RegisterPage:
    def __init__(self, page)->None:
        self.page = page
        self.url = 'https://demo.opencart.com/index.php?route=account/register&language=en-gb'
        self.firstname_input = page.get_by_placeholder("First Name")
        self.lastname_input = page.get_by_placeholder("Last Name")
        self.email_input = page.get_by_placeholder("E-Mail")
        self.pass_input = page.get_by_placeholder("Password")
        self.newsletter_input = page.get_by_role("group", name="Newsletter").locator("div").nth(2)
        self.checkbox_privacy = page.get_by_role("checkbox")
        self.submit_btn = page.get_by_role("button", name="Continue")
        self.subscribe_no = page.get_by_label("No")
        self.subscribe_yes = page.get_by_label("Yes")

    def register_run(self) -> None:
        self.page.goto(self.url)

    def fillOut_form(self, firstname, lastname, email, password, checkbox: bool, label: bool) ->None:
        self.firstname_input.fill(firstname)
        self.lastname_input.fill(lastname)
        self.email_input.fill(email)
        self.pass_input.fill(password)
        if checkbox:
            self.checkbox_privacy.check()
        else:
            pass

        if label:
            self.subscribe_yes.check()
        else:
            self.subscribe_no.check()

        self.submit_btn.click()




