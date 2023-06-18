from pages.login_page import LoginPage

def test_nahla_nadina(driver):

    login_page = LoginPage(driver)
    login_page.go_to()

    login_page.login("standard_user", "secret_sauce")
    assert login_page.product_text() == "Products"
    login_page.add_to_cart()
    assert login_page.your_cart() == "Your Cart"
    assert login_page.verify_product_name("Sauce Labs Backpack") == "Sauce Labs Backpack"
    assert login_page.verify_product_name("Sauce Labs Bike Light") == "Sauce Labs Bike Light"
    login_page.checkout()
    assert login_page.checkout_yi() == "Checkout: Your Information" 
    login_page.checkout_info("Nadina", "Adzovic", "71000")
    assert login_page.checkoutOverview() == "Checkout: Overview"
    assert login_page.verify_product_name("Sauce Labs Backpack") == "Sauce Labs Backpack"
    assert login_page.verify_product_name("Sauce Labs Bike Light") == "Sauce Labs Bike Light"   
    login_page.finish()
    assert login_page.checkoutComplete() == "Checkout: Complete!"  
    login_page.logout()
