import time


class ProductCard:
    def __init__(self, page)->None:
        self.page = page
        self.url = 'https://demo.opencart.com/index.php?route=product/product&language=en-gb&path=24&product_id=28'
        self.addtocart_btn = page.get_by_role("button", name="Add to Cart")
        self.qty = page.get_by_label("Qty")
        self.success_inf = page.locator("xpath=//div[contains(text(), 'Success: You have added')]")
        self.productName = page.locator("xpath=//h1")
    def productcard_run(self)->None:
        self.page.goto(self.url)
    def addtocart(self,qty:int)->None:
        self.qty.fill(f'${qty}')
        self.addtocart_btn.click()

