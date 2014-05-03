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
        driver.find_element_by_xpath('//*[@id="tabs"]/a[2]').click()
        # tab2
        driver.find_element_by_xpath(
            '//*[@id="tab-data"]/table/tbody/tr[1]/td[2]/input'
        ).send_keys(data['title'])
        driver.find_element_by_xpath(
            '//*[@id="tab-data"]/table/tbody/tr[16]/td[2]/input'
        ).send_keys(data['title'].replace(' ', '-'))

        driver.find_element_by_xpath('//*[@id="tabs"]/a[1]').click()
        # tab1
        driver.find_element_by_name(
            "product_description[2][name]"
        ).send_keys(data['title'])

        driver.find_element_by_xpath(
            '//*[@id="language2"]/table/tbody/tr[5]/td[2]/input'
        ).send_keys(data['title'].replace(' ', ','))

        driver.find_element_by_xpath('//*[@id="cke_6"]/span[3]').click()

        desc = driver.find_element_by_xpath(
            '//*[@id="language2"]/table/tbody/tr[3]/td[2]/textarea'
        )
        desc.click()
        desc.send_keys(str(data['description']))



    driver = webdriver.Firefox()
    driver.get(url)

    login(driver)
    add_product(driver)
    fill_form(driver, data)