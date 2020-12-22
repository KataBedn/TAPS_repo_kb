from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('/Users/katab/PycharmProjects/drivers/chromedriver.exe')

website = driver.get('https://fabrykatestow.pl/')

driver.find_element_by_xpath("//li[@id='menu-item-622']//a[contains(text(),'Kursy')]").click()
driver.find_element_by_partial_link_text('PRZEJDŹ DO STRONY KURSU').click()
element = driver.find_element_by_xpath("//h3[contains(text(),'Paweł Zwierzchowski')]")

ActionChains(driver).move_to_element(element).perform()

driver.save_screenshot("screenshot.png")