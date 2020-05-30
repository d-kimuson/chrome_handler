from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from typing import Optional

from .settings import CHROME_DRIVER_PATH


class ChromeHandler:
    """Selenium + Chrome Driverのハンドラ

     スクレイピング用のハンドラです.

    Attributes:
        chrome_driver_path (str): chrome driverが置かれているパス
        is_browser (bool): ブラウザを実際に開くかどうか, 既定値: False

    """
    def __init__(self, chrome_driver_path: str, is_browser: bool = False) -> None:
        """コンストラクタ

        Args:
            chrome_driver_path (str): chrome driverが置かれているパス
            is_browser (bool, optional): ブラウザを実際に開くかどうか, 既定値: False

        Returns:
           None: 戻り値なし

        Note:
            事前に Chrome Driver をインストールする必要あり.
            https://chromedriver.chromium.org/downloads

        """
        op = Options()
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-extensions")
        op.add_argument("--proxy-server='direct://'")
        op.add_argument("--proxy-bypass-list=*")
        op.add_argument("--start-maximized")
        op.add_argument("--headless")

        if is_browser:
            self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        else:
            self.driver = webdriver.Chrome(
                CHROME_DRIVER_PATH, options=op
            )

        self.soup = None

    def __wait__(self, _time: int, key: str, val: str) -> None:
        print("Search Element: ({}, {})".format(key, val))
        WebDriverWait(self.driver, _time).until(
            EC.presence_of_element_located(
                (key, val)
            )
        )

    def wait(self,
             _id: Optional[str] = None,
             cl: Optional[str] = None,
             selector: Optional[str] = None,
             _time: int = 30) -> None:
        """特定の要素がレンダリングされるまで待つ関数

        Args:
            _id (str, optional): 待つ要素のID
            cl (str, optional): 待つ要素のClass
            selector (str, optional): 待つ要素の CSS セレクタ
            _time (str, optioanl): 最大待ち時間

        Returns:
           None: 戻り値なし

        """
        params = [
            (By.ID, _id),
            (By.CLASS_NAME, cl),
            (By.CSS_SELECTOR, selector)
        ]
        for param in params:
            if isinstance(param[1], str):
                self.__wait__(
                    _time, param[0], param[1]
                )

    def access(self,
               url: str,
               _id: Optional[str] = None,
               cl: Optional[str] = None,
               selector: Optional[str] = None) -> None:
        """特定のURLにアクセスする関数

        URLから別のページへアクセスする

        Args:
            url (str): アクセス先のURL
            _id (str, optional): アクセス終了判定用の id
            cl (str, optional): アクセス終了判定用の class
            selector (str, optional): アクセス終了判定用の css selector

        Notes:
            _id, cl, selector が全て None のときはアクセス終了判定をしない

        """
        self.driver.get(url)
        if (_id is not None) or (cl is not None) or (selector is not None):
            self.wait(_id=_id, cl=cl, selector=selector)
        self.set_soup()

    def set_soup(self) -> None:
        """handler 持つ beautiful soup を更新する関数

        chrome で開かれているページソースを元に, self.soup に bs オブジェクトを設置する

        Note:
            ページソースが変わるたびに, これを呼ぶことで beautiful soup を通じてデータの取得ができる

        """
        self.soup = BeautifulSoup(
            self.driver.page_source,
            features="html.parser"
        )

    def fin(self) -> None:
        """終了関数

        """
        self.driver.quit()
