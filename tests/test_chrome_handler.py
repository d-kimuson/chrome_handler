import pytest
import os

from chrome_handler import ChromeHandler


@pytest.fixture
def handler():
    return ChromeHandler(
        is_browser=False,
        chrome_driver_path=os.path.join(
            os.getcwd(), 'tests', 'chromedriver83'
        )
    )


class T_ChromeHandler:
    def case_ChromeDriverの読み込み(self, handler):
        assert True
