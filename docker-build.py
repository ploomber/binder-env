"""
Trigger docker build on binder
"""
import argparse

# https://github.com/jsoma/selenium-github-actions
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# 1200 is fine for binder-env but jupysql needs more time
TIMEOUT = 2400


def build_docker(url):
    print("Initializing Chrome driver...")

    chrome_service = Service(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    )

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
    print("Initialized Chrome driver")

    print("Getting URL...")
    driver.get(url)
    print("Got URL...")

    print("Waiting for JupyterLab redirection...")
    wait.until(EC.title_is("JupyterLab"))
    print("Redirected. Success!")


def main():
    parser = argparse.ArgumentParser(description="Trigger Binder Docker build")
    parser.add_argument("url", help="The URL to process")
    args = parser.parse_args()
    build_docker(args.url)


if __name__ == "__main__":
    main()
