from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class search_add_to_cart_page:

    def __init__(self, context):
        self.driver = context.driver
        self.wait = WebDriverWait(self.driver, 10)

        self.url = "https://adnabu-store-assignment1.myshopify.com"
        self.search_result = "//ul[@id='predictive-search-results-products-list']/li"
        self.cart_quantity = "//input[@aria-label='Quantity for The Multi-location Snowboard']"
        self.cart_drawer = "//h2[text()='Your cart']"
        self.password = "password"
        self.homepage = "//span[@class='header__active-menu-item']"
        self.search_icon = "//*[name()='svg'][contains(@class,'icon-search')]"
        self.search_bar = "Search-In-Modal"
        self.btn_enter = "//button[text()='Enter']"
        self.btn_shop_products = "//a[text()='Shop products']"
        self.btn_add_to_cart = "//button[@name='add']"

    def navigate_to_adnabu_store(self):
        self.driver.get(self.url)

    def enter_store_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.ID, self.password))).send_keys(password)

    def click_on_enter_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_enter))).click()

    def click_on_shop_products_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_shop_products))).click()

    def click_on_add_to_cart_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_add_to_cart))).click()

    def validate_homepage(self):
        homepage_selection = self.wait.until(EC.presence_of_element_located((By.XPATH, self.homepage)))
        assert homepage_selection.is_displayed()

    def click_on_search_icon(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_icon))).click()

    def search_for_product(self, product_name):
        self.wait.until(EC.presence_of_element_located((By.ID, self.search_bar))).send_keys(product_name)

    def validate_search_result(self):
        search_results = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.search_result)))
        assert search_results.is_displayed()

    def click_on_search_result(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_result))).click()

    def verify_product_in_cart(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, self.cart_drawer)))

        cart_quantity = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, self.cart_quantity)
        )).get_attribute("value")

        assert int(str(cart_quantity)) == 1

