def test_first(browser):
    browser.get('http://localhost/')
    assert browser.title == 'Your Store'


def test_second(browser):
    browser.get('https://dzen.ru')
    assert browser.title == 'Дзен'
