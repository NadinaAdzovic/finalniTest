from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains



class LoginPage:

    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()
    
    def login(self, username, password):
        username_field_locator = (By.ID, "user-name")
        username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        username_field.click()
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)
        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()
        
    def product_text(self):
        product_text_tuple = (By.XPATH, "//span[text()='Products']")
        wait_product_text = self.wait.until(EC.element_to_be_clickable(product_text_tuple))
        product_text = wait_product_text.text
        return product_text
    def add_to_cart(self):
        add_to_cart_button1 = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button1.click()
        add_to_cart_button2 = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart_button2.click()
        cart_icon = self.selenium_driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
       

    def your_cart(self):
        your_cart_text_tuple = (By.XPATH, "//span[text()='Your Cart']")
        your_cart_text = self.wait.until(EC.element_to_be_clickable(your_cart_text_tuple))
        your_cart = your_cart_text.text
        return your_cart
   
  
    
    def verify_product_name(self, product_name):
       
        product_name_element = self.selenium_driver.find_element(By.XPATH, f"//div[@class='cart_item']//div[@class='inventory_item_name' and text()='{product_name}']")
        return product_name_element.text    

    
    def checkout(self):
        checkout_button = self.selenium_driver.find_element(By.ID, "checkout")
        checkout_button.click()

    def checkout_yi(self):
        checkoutyi_text_tuple = self.selenium_driver.find_element(By.XPATH, "//span[text()=\"Checkout: Your Information\"]")
        checkoutyi_text = self.wait.until(EC.element_to_be_clickable(checkoutyi_text_tuple))
        checkoutyi = checkoutyi_text.text
        return checkoutyi
    
    def checkout_info(self,name, lastname, zip_code):
        name_field_locator = (By.ID, "first-name")
        name_field = self.wait.until(EC.element_to_be_clickable(name_field_locator))
        name_field.click()
        name_field.clear()
        name_field.send_keys(name)
        lastname_field = self.selenium_driver.find_element(By.ID, "last-name")
        lastname_field.click()
        lastname_field.clear()
        lastname_field.send_keys(lastname)
        zip_code_field_locator = (By.ID, "postal-code")
        zip_code_field = self.wait.until(EC.element_to_be_clickable(zip_code_field_locator))
        zip_code_field.click()
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)
        continue_button = self.selenium_driver.find_element(By.ID, "continue")
        continue_button.click()

    def checkoutOverview(self):
        checkoutov_text_tuple = (By.XPATH, "//span[text()='Checkout: Overview']")
        checkoutov_text = self.wait.until(EC.element_to_be_clickable(checkoutov_text_tuple))
        checkoutov = checkoutov_text.text
        return checkoutov

    def finish(self):
        finish_button = self.selenium_driver.find_element(By.ID, "finish")
        finish_button.click()
    
    def checkoutComplete(self):      
        checkoutcomplete_text_tuple = (By.XPATH, "//span[text()=\"Checkout: Complete!\"]")
        checkoutcomplete_text = self.wait.until(EC.element_to_be_clickable(checkoutcomplete_text_tuple))
        checkoutcomplete = checkoutcomplete_text.text
        return checkoutcomplete
    
    def logout(self):
        menu_button_locator = self.selenium_driver.find_element(By.ID, "react-burger-menu-btn")
        wait_menu_button = self.wait.until(EC.element_to_be_clickable(menu_button_locator))
        wait_menu_button.click()
        logout_button_locator= self.selenium_driver.find_element(By.ID, "logout_sidebar_link")
        wait_logout_button = self.wait.until(EC.element_to_be_clickable(logout_button_locator))
        wait_logout_button.click()

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        


       
           