import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', choices=['chrome', 'firefox', 'safari'])
    parser.addoption('--headless', action='store_true')
    parser.addoption('--base_url', required=True)


@pytest.fixture()
def base_url(request):
    return request.config.getoption('--base_url')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    service = Service()

    if browser_name == 'chrome':
        options = Options()
        if headless:
            options.add_argument('headless=new')
        service = Service(executable_path=os.path.expanduser('~/drivers/chromedriver'))
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == 'safari':
        options = SafariOptions()
        options.headless = headless
        driver = webdriver.Safari(service=service, options=options)
    else:
        raise NotImplementedError

    yield driver
    driver.quit()
