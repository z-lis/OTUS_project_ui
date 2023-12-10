from selenium.webdriver.common.by import By


def test_search_input(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.NAME, 'search').send_keys('test')
    browser.find_element(By.CSS_SELECTOR, '#search > button').click()
    browser.find_element(value='content')
