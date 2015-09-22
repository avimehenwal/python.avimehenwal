import pytest
from selenium.webdriver import firefox

@pytest.fixture
def webdriver(request):
    driver = Firefox()
    request.addfinalizer(driver.quit)
    return driver

def test_title(webdriver):
    webdriver.get('http://python.org')
    assert 'Python' in webdriver.title

def test_pytest_title(webdriver):
    webdriver.get('http://pytest.org/')
    assert 'pytest' in webdriver.title

