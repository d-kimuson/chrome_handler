import os

BASE_DIR = os.getcwd()
CHROME_DRIVER_PATH: str = os.path.join(
    os.path.expanduser('~'), 'Selenium', 'chromedriver'
)
