import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestShopee(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install().find_element_by_xpath("//input[@placeholder='Search in Shopee']"))

     
    def test_a_search_product(self):
        driver = self.browser
        driver.get("https://www.shopee.co.id/") 
        time.sleep(3)
        search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
        search_input.send_keys("phone") 
        time.sleep(1)
        search_button = driver.find_element(By.CLASS_NAME, "btn.btn-solid-primary.btn--s.btn--inline")
        search_button.click()
        time.sleep(1)
        
        # Validation - check if search results are displayed
        result_count = driver.find_element(By.CLASS_NAME, "_22sp0A")
        self.assertIsNotNone(result_count.text)

    def test_b_add_to_cart(self):
        driver = self.browser
        driver.get("https://www.shopee.co.id/") 
        time.sleep(3)
        search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
        search_input.send_keys("laptop") 
        time.sleep(1)
        search_button = driver.find_element(By.CLASS_NAME, "btn.btn-solid-primary.btn--s.btn--inline")
        search_button.click()
        time.sleep(1)
        
        # Select the first product from the search results
        product_link = driver.find_element(By.CLASS_NAME, "O6wiAW")
        product_link.click()
        time.sleep(1)
        
        # Add the product to the cart
        add_to_cart_button = driver.find_element(By.CLASS_NAME, "_1gkBDw._2O43P5")
        add_to_cart_button.click()
        time.sleep(1)
        
        # Validation - check if the cart has at least one item
        cart_count = driver.find_element(By.CLASS_NAME, "_16nzq18")
        self.assertNotEqual(cart_count.text, '0')

    def test_c_checkout(self):
        driver = self.browser
        driver.get("https://www.shopee.co.id/") 
        time.sleep(3)
        search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
        search_input.send_keys("shirt") 
        time.sleep(1)
        search_button = driver.find_element(By.CLASS_NAME, "btn.btn-solid-primary.btn--s.btn--inline")
        search_button.click()
        time.sleep(1)
        
        # Select the first product from the search results
        product_link = driver.find_element(By.CLASS_NAME, "O6wiAW")
        product_link.click()
        time.sleep(1)
        
        # Add the product to the cart
        add_to_cart_button = driver.find_element(By.CLASS_NAME, "_1gkBDw._2O43P5")
        add_to_cart_button.click()
        time.sleep(1)
        
        # Go to the cart
        cart_button = driver.find_element(By.CLASS_NAME, "btn.btn-solid-primary.btn--l.YtgjXY")
        cart_button.click()
        time.sleep(1)
        
        # Proceed to checkout
        checkout_button = driver.find_element(By.CLASS_NAME, "shopee-button-solid.shopee-button-solid--primary.shopee-button-solid--jss-3")
        checkout_button.click()
        time.sleep(1)
        
        # Validation - check if the checkout page is displayed
        checkout_title = driver.find_element(By.CLASS_NAME, "checkout-title")
        self.assertIsNotNone(checkout_title.text)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
