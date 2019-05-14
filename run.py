from splinter import Browser
from time import sleep, strftime
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import pickledb

username = 'XXXX'
password = 'XXXX'
domain_only = True

chrome_options = Options()
for x in ['ext/1.crx', 'ext/2.crx', 'ext/3.crx']:
    chrome_options.add_extension(x)

with Browser('chrome', chrome_options=chrome_options) as browser:
    browser.visit("https://www.alexa.com/toolbar/final?session=DEFAULT_ALX_ID&plugin=4.0.3")
    sleep(3)
    browser.visit("https://rankboostup.com/login")
    browser.fill('username', username)
    browser.fill('password', password)
    browser.find_by_xpath('//*[@id="submit-form"]').click()
    sleep(3)
    browser.visit("https://rankboostup.com/dashboard/traffic-exchange/")

    while 1:
        sleep(1)
        if browser.is_element_present_by_css('.start-exchange-boostup'):
            browser.find_by_css('.start-exchange-boostup').click()
            print('start button')
            break
        else:
            sleep(1)
            if browser.is_element_present_by_text(' Cancel Session'):
                browser.find_by_css('.btn-danger').click()
            print('no start button')

    while 1:
        sleep(1)
        if browser.is_element_present_by_css('.sa-confirm-button-container'):
            browser.find_by_xpath('/html/body/div[2]/div[7]/div/button').click()
            print('activate button')
            break
        else:
            sleep(1)
            print('no activate button')

    old_url = ''
    while 1:
        try:
            db_name = strftime('%d|%m|%Y')
            db = pickledb.load(f'data/{db_name}.db', False)
            sleep(10)
            url = browser.windows[1].url
            if domain_only:
                url = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))
            if old_url != url:
                if not db.exists(url):
                    db.set(url, 1)
                else:
                    db.set(url, db.get(url) + 1)
                print(f'{url}')
                db.dump()
                old_url = url
        except Exception as e:
            pass
