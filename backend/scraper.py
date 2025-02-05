from selenium import webdriver
from selenium.webdriver.common.by import By

def fetch_prices(grocery_list):
    driver = webdriver.Chrome()
    data = {}

    for item in grocery_list:
        url = f"https://www.blinkit.com/s/?q={item}"
        driver.get(url)

        try:
            product_name = driver.find_element(By.CLASS_NAME, "product-name").text
            price = driver.find_element(By.CLASS_NAME, "product-price").text
            data[item] = {"store": "Blinkit", "price": price, "name": product_name}
        except:
            data[item] = {"store": "Blinkit", "price": "Not Found"}

    driver.quit()
    return data
