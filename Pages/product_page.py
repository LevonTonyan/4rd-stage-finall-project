from .base_page import BasePage
from Pages.locators import BasketPageLocators
from Pages.locators import MainPageLocators


class ProductPage(BasePage):

    def add_item_to_basket(self):
        self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON).click()

    def item_was_added(self):
        output = self.browser.find_element(*BasketPageLocators.HAS_BEEN_ADDED)
        assert "has been added to your basket" in output.text, 'THE ITEM WAS NOT ADDED TO THE BASKET'

    def correct_item_was_added(self):
        added_item_name = self.browser.find_element(*BasketPageLocators.ADDED_ITEM_NAME)
        real_item = self.browser.find_element(*BasketPageLocators.REAL_ITEM_NAME)
        assert added_item_name.text == real_item.text, 'WRONG ITEM WAS ADDED TO THE BASKET'
