from selenium import webdriver

from ..settings import chrome_driver, url, admin


def upload_data(data):
    def login(driver):
        driver.find_element_by_name("username").send_keys(admin['user'])
        driver.find_element_by_name("password").send_keys(admin['pass'])
        driver.find_element_by_class_name("button").click()

    def add_product(driver):
        part = '//*[@id="catalog"]/'
        driver.find_element_by_xpath('{}a'.format(part)).click()
        driver.find_element_by_xpath('{}ul/li[2]/a'.format(part)).click()
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/a[1]').click()

    def fill_form(driver, data):
        js_script = "d = document.getElementsByTagName('pre');\
            d[1].innerHTML = '{}';".format(data['description'])

        driver.find_element_by_name("product_description[2][name]").send_keys(data['title'])
        driver.find_element_by_xpath('//*[@id="cke_6"]/span[3]').click()
        driver.find_element_by_xpath('//*[@id="cke_1_contents"]').click()
        driver.execute_script(js_script)

    driver = webdriver.Chrome(chrome_driver)
    driver.get(url)

    login(driver)
    add_product(driver)
    fill_form(driver, data)
