from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form!']")
    REG_FORM = (By.CSS_SELECTOR, "form[id='register_form!']")



class BasketPageLocators():
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "div[id='messages'] >div:first-child > div[class='alertinner '] > strong")
    HAS_BEEN_ADDED = (By.CSS_SELECTOR, "div[id='messages'] >div:first-child > div[class='alertinner ']")
    REAL_ITEM_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] > h1")