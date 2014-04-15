from selenium import webdriver

from ..settings import chrome_driver, url


def upload_data(data):
    def login(driver):
        driver.find_element_by_name("username").send_keys("demo")
        driver.find_element_by_name("password").send_keys("demo")
        driver.find_element_by_class_name("button").click()

    def add_product(driver):
        driver.find_element_by_xpath('//*[@id="catalog"]/a').click()
        driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/a[1]').click()

    driver = webdriver.Chrome(chrome_driver)
    driver.get(url)

    login(driver)
    add_product(driver)
