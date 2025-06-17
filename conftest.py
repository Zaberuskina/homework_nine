import pytest
from selene.support.shared import browser

@pytest.fixture(autouse=True, scope='function')
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1200
    browser.config.window_height = 1000
    yield
    browser.quit()
