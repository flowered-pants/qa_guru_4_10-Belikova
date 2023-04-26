import socket
import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    sock = socket.socket()
    sock.settimeout(20)
    browser.config.hold_browser_open = True
    browser.config.type_by_js = True
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = ('https://demoqa.com')
    yield