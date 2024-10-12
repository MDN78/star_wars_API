import allure

@allure.feature('Shop')
class TestProduct:

    def test_product(self, customer):
        print(customer)

    def test_bascet(self, customer):
        print(customer)