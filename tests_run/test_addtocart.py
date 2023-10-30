import pytest

from DOMs.productcard_page import ProductCard


def test_productCart(page)->None:
    productcart = ProductCard(page)
    productcart.productcard_run()
    productcart.addtocart(1)