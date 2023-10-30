class CategoryPage:
    def __init__(self, page) -> None:
        # Inicjacja obiektów, przyciskow na stronie głównej
        self.page = page
        self.cat = page.get_by_role("link", name="Cameras")
        self.product_on_list_H4 = page.get_by_text("$98.00").first.locator('xpath=../..//h4').text_content()

    def category_open_by_menu(self) -> None:
        # Wykonywanie akcji, które uruchamiamy jako testy
        self.cat.click()

    def products_list_test(self) -> None:
        h4 = self.product_on_list_H4
        print(h4)
        self.product_on_list_H4.click()
