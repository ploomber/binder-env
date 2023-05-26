"""
Trigger docker build on binder
"""
# https://github.com/jsoma/selenium-github-actions
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

# I timed the process one time and it took 7 mins 10 seconds. Adding a
# buffer
TIMEOUT = 1200

print('Initializing Chrome driver...')

chrome_service = Service(
    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

wait = WebDriverWait(driver, TIMEOUT)
print('Initialized Chrome driver')

print('Getting URL...')
url = 'https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252FREADME.ipynb%26branch%3Dmaster'
driver.get(url)
print('Got URL...')

print('Waiting for JupyterLab redirection...')
wait.until(EC.title_is('JupyterLab'))
print('Redirected. Success!')
