"""
Trigger docker build on binder
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

print('Initializing Chrome driver...')
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 120)
print('Initialized Chrome driver')

print('Getting URL...')
url = 'https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252FREADME.ipynb%26branch%3Dmaster'
driver.get(url)
print('Got URL...')

print('Waiting for JupyterLab redirection...')
wait.until(EC.title_is('JupyterLab'))
print('Redirected. Success!')
