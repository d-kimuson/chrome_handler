import os

BASE_DIR = os.getcwd()
BASE_URL: str = ""
CHROME_DRIVER_PATH: str = os.path.join(
    os.path.expanduser('~'), 'Selenium', 'chromedriver'
)

TIME_SPAN = 1  # アクセス秒間隔, 対象サイト負荷軽減のため一定より大きくすること
